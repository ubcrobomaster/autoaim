from source.module import Module
from pathlib import Path
import serial
import time
import os


class Uart(Module):
	def __init__(self, parent=None, state=None):
		self.working_dir = Path(os.path.dirname(os.path.abspath(__file__)))
		super().__init__(self.working_dir, parent=parent, state=state)
		self.ser = serial.Serial(
			port='/dev/serial0' ,\
			baudrate=115200,\
			parity=serial.PARITY_NONE,\
			stopbits=serial.STOPBITS_ONE,\
			bytesize=serial.EIGHTBITS,\
				timeout=0)

	def read_buffer(self):
		received_data = self.ser.read()
		time.sleep(0.03)
		data_left = self.ser.inWaiting()
		received_data += self.ser.read(data_left)
		print(received_data.decode())
		return received_data.decode()

	def twos_complement(self, hexstr, bits):
		value = int(hexstr,16)
		if value & (1 << (bits-1)):
			value -= 1 << bits
		return value

	#TO-DO add error checking
	def read_hex(self):
		str_num = self.read_buffer()
		
		if len(str_num) == 0:
			print("buffer empty")
			return 0
		
		stripped_chars = str_num.rstrip("\n\r")
		num_bits = len(stripped_chars)*4
		#hex_num_str = '0x'+()
		#hex_num = int(hex_num_str, 16)
		s_hex_num = self.twos_complement(stripped_chars, num_bits)
		#print(hex_num_str + ": " + str(hex_num))
		print(s_hex_num)
		return s_hex_num

	def send_hex(self, angle):
		if angle < 0:
			hex_str = hex(65536+angle)
		else:
			hex_str = hex(angle)
		#hex_str = "{0:b}".format(angle)
		#print(hex(self.twos_complement(angle))) 
		#self.send_string(hex(self.twos_complement(angle)))
		#print(hex_str)
		self.send_string(hex_str + '\r\n')

	def send_string(self, data_out=None):
		if data_out is None:
			data = input("Type: ")
			if data == "":
				print("Data must not be null")
				return False
			else:
				self.ser.write(data.encode())
		else:
			self.ser.write(data_out.encode())
		return True

