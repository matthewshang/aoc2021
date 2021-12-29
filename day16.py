import binascii
import operator
from functools import reduce


class Packet:
    def __init__(self, version: int, type_id: int):
        self.version = version
        self.type_id = type_id
        self.contents = None

    def eval(self) -> int:
        return 0


class LiteralPacket(Packet):
    def __init__(self, version: int, value: int):
        super().__init__(version, 4)
        self.contents = value

    def eval(self) -> int:
        return self.contents


class OperatorPacket(Packet):
    def __init__(self, version: int, type_id: int, subpackets: list[Packet]):
        super().__init__(version, type_id)
        self.contents = subpackets

    def eval(self) -> int:
        results = [subpacket.eval() for subpacket in self.contents]
        match self.type_id:
            case 0: return reduce(operator.add, results)
            case 1: return reduce(operator.mul, results, 1)
            case 2: return reduce(min, results)
            case 3: return reduce(max, results)
            case 5: return results[0] > results[1]
            case 6: return results[0] < results[1]
            case 7: return results[0] == results[1]


class Parser:
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0

    def read_bit(self) -> int:
        shift = 7 - self.pos % 8
        bit = self.data[self.pos // 8] & (1 << shift)
        self.pos += 1
        return bit >> shift

    def read_fixed_size(self, len: int) -> int:
        value = 0
        while len:
            value = 2 * value + self.read_bit()
            len -= 1
        return value

    def read_header(self) -> tuple[int, int]:
        return self.read_fixed_size(3), self.read_fixed_size(3)

    def read_literal_value(self) -> int:
        value = 0
        active = 1
        while active:
            active &= self.read_bit()
            value = value * 16 + self.read_fixed_size(4)
        return value

    def read_operator_total_length(self, length: int) -> list[Packet]:
        stop_pos = self.pos + length
        packets = []
        while self.pos < stop_pos:
            packets.append(self.read_packet())
        return packets

    def read_operator_subpackets(self, num: int) -> list[Packet]:
        return [self.read_packet() for _ in range(num)]

    def read_packet(self) -> Packet:
        version, type_id = self.read_header()
        match type_id:
            case 4:
                value = self.read_literal_value()
                return LiteralPacket(version, value)
            case _:
                length_type_id = self.read_bit()
                if length_type_id == 0:
                    length = self.read_fixed_size(15)
                    subpackets = self.read_operator_total_length(length)
                    return OperatorPacket(version, type_id, subpackets)
                else:
                    num = self.read_fixed_size(11)
                    subpackets = self.read_operator_subpackets(num)
                return OperatorPacket(version, type_id, subpackets)


def add_versions(packet: Packet) -> int:
    sum = packet.version
    match packet:
        case OperatorPacket(contents=subpackets):
            for subpacket in subpackets:
                sum += add_versions(subpacket)
    return sum


data = binascii.unhexlify(open('day16.txt').readline().strip())
parser = Parser(data)
root = parser.read_packet()
print(f'Part 1: {add_versions(root)}')
print(f'Part 2: {root.eval()}')
