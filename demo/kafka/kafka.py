# coding: utf-8
import json
import time
import uuid
from datetime import datetime
from functools import partial
from threading import Thread

from icecream import ic

from zbtest import world
from pykafka import KafkaClient

# from zbtest.utils.logs import file_logger
print_now = partial(print, flush=True)

now = datetime.now()

# consumers = {
#     'car_in': [],
#     'car_out': [],
#     'after_pay': [],
#     'record_update': [],
# }

# topics = dict.fromkeys(['car_in', 'car_out', 'after_pay', 'record_update'])
consumers = {}
topics = {}

topic_mapping = dict(
    car_in='parkingRecordIn',
    car_out='parkingRecordOut',
    after_pay='topic_afterpay_send_order_kafka',
    record_update='parkingRecordUpdate'
)


class Signal(object):
    def __init__(self):
        self.__flag = False
        self.__running = set()

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, value):
        self.__flag = value

    @property
    def running(self):
        return self.__running


signal = Signal()


def init_consumers():
    # file_logger.debug('initializing kafka consumers...')
    print_now('initializing kafka consumers...')
    client = KafkaClient(hosts='10.103.22.89:9093,10.103.22.92:9093,10.103.22.93:9093')

    for nick, name in topic_mapping.items():
        topic = client.topics[name]
        consumer = topic.get_simple_consumer(consumer_group='mock')
        consumer.reset_offsets([(p, now) for p in consumer.partitions.values()])
        topics[nick] = topic
        consumers[nick] = consumer


kafka_msg = {
    'parkingRecordIn': {},
    'parkingRecordOut': {},
    'topic_afterpay_send_order_kafka': {},
    'parkingRecordUpdate': {},
}


class KfkCbkRegistry(dict):
    def append_to(self, topic, handler):
        self.setdefault(topic, set()).add(handler)

    def remove_from(self, topic, handler):
        if topic in self:
            self[topic].discard(handler)

    def clear(self, topic=None):
        if topic:
            self.pop(topic)
        else:
            super().clear()


KAFKA_CBK_REGISTRY = KfkCbkRegistry()


def kfk_msg_cbk(topic, *args, **kwargs):
    return lambda func: KAFKA_CBK_REGISTRY.append_to(topic, partial(func, *args, **kwargs))


def consume_kafka_msg(nick, name):
    def middle(func):
        def wrapped(park_id, **kwargs):
            print_now(f'start polling consumer {nick}...')
            for message in consumers[nick]:
                if signal.flag:
                    print_now(f'not consuming {nick}')
                    break
                ic(message.value)
                param = json.loads(message.value)['param']
                kwargs.update(param=param, nick=nick, name=name)
                if message is not None:
                    func(park_id, **kwargs)
            print_now(f'consumer {nick} over')
            signal.running.discard(name)
        return wrapped
    return middle


@consume_kafka_msg('car_in', 'parkingRecordIn')
def consume_car_in_(park_id, param, nick, name):
    if param['parkId'] == park_id:
        print_now(f'{nick}: {param}')
        kafka_msg[name][param['synId'].lower()] = param
        for cbk in KAFKA_CBK_REGISTRY.get(name, []):
            cbk(param)


@consume_kafka_msg('car_out', 'parkingRecordOut')
def consume_car_out_(park_id, param, nick, name):
    if param['parkId'] == park_id:
        print_now(f'{nick}: {param}')
        kafka_msg[name][param['synId'].lower()] = param
        for cbk in KAFKA_CBK_REGISTRY.get(name, []):
            cbk(param)


@consume_kafka_msg('after_pay', 'topic_afterpay_send_order_kafka')
def consume_after_pay_(park_id, param, nick, name):
    order = json.loads(param)['order']
    if order['parkingId'] == park_id:
        print_now(f'{nick}: {param}')
        kafka_msg[name].setdefault(order['orderId'].lower(), []).append(param)
        for cbk in KAFKA_CBK_REGISTRY.get(name, []):
            cbk(param)


@consume_kafka_msg('record_update', 'parkingRecordUpdate')
def consume_record_update_(park_id, param, nick, name):
    if param['parkId'] == park_id:
        print_now(f'{nick}: {param}')
        kafka_msg[name][param['synId'].lower()] = param
        for cbk in KAFKA_CBK_REGISTRY.get(name, []):
            cbk(param)


def consume_car_in(park_id):
    # file_logger.debug('start polling consumer car in...')
    print_now('start polling consumer car in...')
    for message in consumers['car_in']:
        if signal.flag:
            print_now('not consuming car in')
            break
        param = json.loads(message.value)['param']
        if message is not None and param['parkId'] == park_id:
            print_now(f'car_in: {message.value}')
            kafka_msg['parkingRecordIn'][param['synId'].lower()] = param
            for cbk in KAFKA_CBK_REGISTRY.get('parkingRecordIn', []):
                cbk(param)
    print_now('consumer car in over')
    signal.running.discard('parkingRecordIn')


def consume_car_out(park_id):
    # file_logger.debug('start polling consumer car out...')
    print_now('start polling consumer car out...')
    for message in consumers['car_out']:
        if signal.flag:
            print_now('not consuming car out')
            break
        param = json.loads(message.value)['param']
        if message is not None and param['parkId'] == park_id:
            print_now(f'car_out: {message.value}')
            kafka_msg['parkingRecordOut'][param['synId'].lower()] = param
            for cbk in KAFKA_CBK_REGISTRY.get('parkingRecordOut', []):
                cbk(param)
    print_now('consumer car out over')
    signal.running.discard('parkingRecordOut')


def consume_after_pay(park_id):
    # file_logger.debug('start polling consumer after pay...')
    print_now('start polling consumer after pay...')
    for message in consumers['after_pay']:
        if signal.flag:
            print_now('not consuming after pay')
            break
        param = json.loads(message.value)['param']
        order = json.loads(param)['order']
        if message is not None and order['parkingId'] == park_id:
            print_now(f'after_pay: {message.value}')
            kafka_msg['topic_afterpay_send_order_kafka'].setdefault(order['orderId'].lower(), []).append(param)
            for cbk in KAFKA_CBK_REGISTRY.get('topic_afterpay_send_order_kafka', []):
                cbk(param)
    print_now('consumer after pay over')
    signal.running.discard('topic_afterpay_send_order_kafka')


def consume_record_update(park_id):
    # file_logger.debug('start polling consumer car out...')
    print_now('start polling consumer record update...')
    for message in consumers['record_update']:
        if signal.flag:
            print_now('not consuming record update')
            break
        param = json.loads(message.value)['param']
        if message is not None and param['parkId'] == park_id:
            print_now(f'record_update: {message.value}')
            kafka_msg['parkingRecordUpdate'][param['synId'].lower()] = param
            for cbk in KAFKA_CBK_REGISTRY.get('parkingRecordUpdate', []):
                cbk(param)
    print_now('consumer record update over')
    signal.running.discard('parkingRecordUpdate')


def start_consuming_kafka_for_park(park_id):
    signal.flag = False
    cci = Thread(target=consume_car_in_, args=(park_id,))
    cco = Thread(target=consume_car_out_, args=(park_id,))
    cap = Thread(target=consume_after_pay_, args=(park_id,))
    cru = Thread(target=consume_record_update_, args=(park_id,))
    for name in topics.values():
        signal.running.add(name)
    for thread in cci, cco, cap, cru:
        thread.start()


def kafka_consuming_stopped():
    return not bool(signal.running)


def has_kafka_msg(topic, key=None):
    if kafka_msg.get(topic):
        if key is not None:
            return key.lower() in kafka_msg[topic]
        else:
            return True
    return False


def get_kafka_msg(topic, key, count_down=5):
    msg = None
    while count_down and not msg:
        msg = kafka_msg[topic].pop(key.lower(), None)
        if msg:
            return msg
        time.sleep(1)
        count_down -= 1
        if not count_down % 5:
            # file_logger.debug('{count_down}s elapsed trying to fetch kafka message...'.format(count_down=count_down))
            print_now(f'{count_down}s elapsed trying to fetch kafka message...')


def produce_car_in(park_name, plate_number, park_id, area_id, box_id, road_id, plate_color=1, park_type=77):
    with topics['car_in'].get_sync_producer() as producer:
        dt_fmt = '%Y%m%d%H%M%S%f'
        epoch = datetime.fromtimestamp(0)
        time_in = datetime.now()
        img = u'{pn}_{ts}_in.jpg'.format(pn=plate_number, ts=time_in.strftime(dt_fmt)[:18])
        syn_id = str(uuid.uuid1())
        if hasattr(world, 'record_syncid'):
            world.record_syncid.setdefault(plate_number, []).append(syn_id)
        msg = {
            'param': {
                'entranceTime': int((time_in - epoch).total_seconds() * 1000),
                'parkName': park_name,
                'exitRoad': 0,
                'onServerTime': int(time.time() * 1000),
                'entranceParkBoxId': box_id,
                'exitCarPlateColor': 0,
                'plateNumber': plate_number,
                'type': str(park_type),
                'exitParkBoxId': 0,
                'parkId': park_id,
                'synId': syn_id,
                'exitCarImageBelieve': 0,
                'entranceCarImage': img,
                'parkingSecondRecord': [],
                'entranceCarImageBelieve': 100,
                'exitTime': -25200000,
                'entranceCarPlateColor': plate_color,
                'entranceAreaId': area_id,
                'entranceRoad': road_id
            },
            'uuid': str(uuid.uuid1())
        }
        producer.produce(json.dumps(msg, separators=(',', ':'), ensure_ascii=False).encode('utf-8'))
    return time_in


def produce_car_out(park_name, plate_number, park_id, time_in,
                    area_id_in, box_id_in, road_id_in, road_in,
                    box_id_out, box_out, road_id_out, road_out,
                    receivable_fee=0, actual_fee=0,
                    plate_color_in=1, plate_color_out=1,
                    park_type=77, syn_id=None):
    with topics['car_out'].get_sync_producer() as producer:
        dt_fmt = '%Y%m%d%H%M%S%f'
        epoch = datetime.fromtimestamp(0)
        time_out = datetime.now()
        img_in = f'{plate_number}_{time_in.strftime(dt_fmt)[:18]}_in.jpg'
        img_out = f'{plate_number}_{time_in.strftime(dt_fmt)[:18]}_out.jpg'
        syn_id = syn_id or str(uuid.uuid1())
        if hasattr(world, 'record_syncid'):
            if syn_id not in world.record_syncid.setdefault(plate_number, []):
                world.record_syncid[plate_number].append(syn_id)
        msg = {
            'param': {
                'couponFee': 0,
                'centerFee': 0,
                'exitRoadName': road_out,
                'receivableFee': receivable_fee,
                'parkName': park_name,
                'businessId': 0,
                'entranceParkBoxId': box_id_in,
                'integralsFee': 0,
                'cpmFee': 0,
                'onlineFee': 0,
                'type': str(park_type),
                'couponId': 0,
                'useType': 0,
                'exitParkBoxId': box_id_out,
                'parkId': park_id,
                'synId': syn_id,
                'parkingSecondRecord': [],
                'entranceCarImageBelieve': 99,
                'entranceCarPlateColor': plate_color_in,
                'cartypeName': '小汽车',
                'loseMoney': 0,
                'cardFee': 0,
                'cartypeId': 4556,
                'adminId': 6128,
                'buscardFee': 0,
                'state': 0,
                'actualFee': actual_fee,
                'isFixed': park_type,
                'useCouponParkingBoxid': 0,
                'entranceTime': int((time_in - epoch).total_seconds() * 1000),
                'exitRoad': road_id_out,
                'entranceRoadName': road_in,
                'exitParkingBoxName': box_out,
                'onServerTime': int(time.time() * 1000),
                'exitCarPlateColor': plate_color_out,
                'plateNumber': plate_number,
                'exitCarImageBelieve': 0,
                'entranceCarImage': img_in,
                'realName': '白老头',
                'exitTime': int((time_out - epoch).total_seconds() * 1000),
                'exitCarImage': img_out,
                'entranceAreaId': area_id_in,
                'entranceRoad': road_id_in
            },
            'uuid': str(uuid.uuid1())
        }
        producer.produce(json.dumps(msg, separators=(',', ':'), ensure_ascii=False).encode('utf-8'))


if __name__ == '__main__':
    init_consumers()
    start_consuming_kafka_for_park(1003591)
