import numpy as np
import time

def convert_time(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    formatted = {
        "d": d, "h": h, "m": m, "s": s, "time": time
    }
    return formatted


def get_packet_size():
    size = 0
    for i in packet:
        if "size" in i:
            size += i["size"]
    return size


def convert_voltage(value):
    voltage_conversion_constant = 40.0
    return value / voltage_conversion_constant


def convert_current(value):
    current_conversion_constant = 125.0
    return value / current_conversion_constant


packet = [
    # ***************General Purpose and OBC********************
    {"group_name": "General Purpose and OBC"},
    {"field": "CallSign", "size": 48, "type": "char", "unit": None, "description": "Satellite Callsign: "},
    {"field": "mission_time", "size": 32, "type": "uint", "unit": 's',
     "description": "Mission Time: {d} days {h} hours {m} minutes {s} seconds ({time} s)"},
    {"field": "boot_counter", "size": 8, "type": "uint", "unit": None, "description": "OBC boot counter: "},
    {"field": "obc_reset_flags", "size": 8, "type": "uint", "unit": None, "description": "OBC reset flags: "},
    {"field": "up_time", "size": 32, "type": "uint", "unit": 's',
     "description": "OBC up time: {d} days {h} hours {m} minutes {s} seconds ({time} s)"},
    {"field": "filesystem_error_counter", "size": 16, "type": "uint", "unit": None,
     "description": "Number of file system errors: "},
    {"field": "last_fs_error_code", "size": 8, "type": "uint", "unit": None,
     "description": "Last file system error code: "},

    # ****************** UHF **************************************
    {"group_name": "UHF"},
    {"field": "baud_rate", "size": 16, "type": "uint", "unit": 'baud', "description": "Transmission baud rate: "},
    {"field": "transmitter_uptime", "size": 32, "type": "uint", "unit": 's',
     "description": "Transceiver up time: {d} days {h} hours {m} minutes {s} seconds ({time} s)"},
    {"field": "transceiver_temp", "size": 8, "type": "int", "unit": "deg C",
     "description": "Transceiver temperature (degrees Celsius): "},

    # ******************** Antenna ************************************
    {"group_name": "Antenna"},
    {"field": "comm_reserved", "size": 4, "type": "bit", "bit_position": 0},
    {"field": "ant_4_switch_status", "size": 1, "type": "bit", "unit": None, "bit_position": 4,
     "description": "Antena #4 switch status: "},
    {"field": "ant_3_switch_status", "size": 1, "type": "bit", "unit": None, "bit_position": 5,
     "description": "Antena #3 switch status: "},
    {"field": "ant_2_switch_status", "size": 1, "type": "bit", "unit": None, "bit_position": 6,
     "description": "Antena #2 switch status: "},
    {"field": "ant_1_switch_status", "size": 1, "type": "bit", "unit": None, "bit_position": 7,
     "description": "Antena #1 switch status: "},

    # **************************** EPS **********************************
    {"group_name": "EPS"},

    # **************************** Solar Panels *************************
    {"sub_group_name": "Solar Panels"},
    {"field": "temperature_x_plus", "size": 8, "type": "int", "unit": "deg C",
     "description": "X plus side panel temperature (degrees Celsius): "},
    {"field": "temperature_x_minus", "size": 8, "type": "int", "unit": "deg C",
     "description": "X minus side panel temperature (degrees Celsius): "},
    {"field": "temperature_y_plus", "size": 8, "type": "int", "unit": "deg C",
     "description": "Y plus side panel temperature (degrees Celsius): "},
    {"field": "temperature_y_minus", "size": 8, "type": "int", "unit": "deg C",
     "description": "Y minus side panel temperature (degrees Celsius): "},
    {"field": "temperature_z_plus", "size": 8, "type": "int", "unit": "deg C",
     "description": "Z plus side panel temperature (degrees Celsius): "},
    {"field": "temperature_z_minus", "size": 8, "type": "int", "unit": "deg C",
     "description": "Z minus side panel temperature (degrees Celsius): "},
    {"field": "sun_sensor_x_plus", "size": 8, "type": "int" , "unit": "deg",
     "description": "X plus side panel sun sensor (degrees): "},
    {"field": "sun_sensor_x_minus", "size": 8, "type": "int", "unit": "deg",
     "description": "X minus side panel sun sensor (degrees): "},
    {"field": "sun_sensor_y_plus", "size": 8, "type": "int", "unit": "deg",
     "description": "Y plus side panel sun sensor (degrees): "},
    {"field": "sun_sensor_y_minus", "size": 8, "type": "int", "unit": "deg",
     "description": "Y minus side panel sun sensor (degrees): "},
    {"field": "sun_sensor_z_plus", "size": 8, "type": "int", "unit": "deg",
     "description": "Z plus side panel sun sensor (degrees): "},
    {"field": "sun_sensor_z_minus", "size": 8, "type": "int", "unit": "deg",
     "description": "Z minus side panel sun sensor (degrees): "},
    {"field": "solar_voltage_x", "size": 8, "type": "uint", "unit": "V", "description": "X axis panels voltage (V): ",
     "conversion": convert_voltage},
    {"field": "solar_current_x_minus", "size": 8, "type": "uint", "unit": "A",
     "description": "X minus panel current (A): ", "conversion": convert_current},
    {"field": "solar_current_x_plus", "size": 8, "type": "uint", "unit": "A",
     "description": "X plus panel current (A): ", "conversion": convert_current},
    {"field": "solar_voltage_y", "size": 8, "type": "uint", "unit": "V", "description": "Y axis panels voltage (V): ",
     "conversion": convert_voltage},
    {"field": "solar_current_y_minus", "size": 8, "type": "uint", "unit": "A",
     "description": "Y minus panel current (A): ", "conversion": convert_current},
    {"field": "solar_current_y_plus", "size": 8, "type": "uint", "unit": "A",
     "description": "Y plus panel current (A): ", "conversion": convert_current},
    {"field": "solar_voltage_z", "size": 8, "type": "uint", "unit": "V", "description": "Z axis panels voltage (V): ",
     "conversion": convert_voltage},
    {"field": "solar_current_z_minus", "size": 8, "type": "uint", "unit": "A",
     "description": "Z minus panel current (A): ", "conversion": convert_current},
    {"field": "solar_current_z_plus", "size": 8, "type": "uint", "unit": "A",
     "description": "Z plus panel current (A): ", "conversion": convert_current},

    # ******************************** Batteries *****************************
    {"sub_group_name": "Batteries"},
    {"field": "batt_pack_voltage", "size": 8, "type": "uint", "unit": "V", "description": "Battery pack voltage (V): ",
     "conversion": convert_voltage},
    {"field": "batt_current", "size": 8, "type": "uint", "unit": "A", "description": "Current on the battery bus (A): ",
     "conversion": convert_current},
    {"field": "temp_bat1", "size": 8, "type": "int", "unit": "deg C",
     "description": "Battery #1 temperature (degrees Celsius): "},
    {"field": "temp_bat2", "size": 8, "type": "int", "unit": "deg C",
     "description": "Battery #2 temperature (degrees Celsius): "},

    # ******************************* EPS busses ****************************
    {"sub_group_name": "EPS busses"},
    {"field": "bcr_bus_voltage", "size": 8, "type": "uint", "unit": "V",
     "description": "Battery Charger Regulator bus voltage (V): ", "conversion": convert_voltage},
    {"field": "bcr_bus_current", "size": 8, "type": "uint", "unit": "A",
     "description": "Battery Charger Regulator bus current (A): ", "conversion": convert_current},
    {"field": "bus_current_5v", "size": 8, "type": "uint", "unit": "A",
     "description": "5V bus current (A): ", "conversion": convert_current},
    {"field": "bus_current_33v", "size": 8, "type": "uint", "unit": "A",
     "description": "3.3V bus current (A): ", "conversion": convert_current},
    {"field": "lup5_state", "size": 1, "type": "bit", "unit": None, "bit_position": 0,
     "description": "Latch-up 5V state: "},
    {"field": "lup33_state", "size": 1, "type": "bit", "unit": None, "bit_position": 1,
     "description": "Latch-up 3.3V state: "},
    {"field": "on_off_power_bus_5", "size": 1, "type": "bit", "unit": None, "bit_position": 2,
     "description": "5V bus state: "},
    {"field": "on_off_power_bus_33", "size": 1, "type": "bit", "unit": None, "bit_position": 3,
     "description": "3.3V bus state: "},
    {"field": "EPS_reserved", "size": 4, "type": "bit", "bit_position": 4},
    {"field": "critical_flag_max_bat2_temp", "size": 1, "type": "bit", "unit": None, "bit_position": 0,
     "description": "Critical Flag maximal bat #2 temperature: "},
    {"field": "critical_flag_min_bat2_temp", "size": 1, "type": "bit", "unit": None, "bit_position": 1,
     "description": "Critical Flag minimal bat #2 temperature: "},
    {"field": "critical_flag_max_bat1_temp", "size": 1, "type": "bit", "unit": None, "bit_position": 2,
     "description": "Critical Flag maximal bat #1 temperature: "},
    {"field": "critical_flag_min_bat1_temp", "size": 1, "type": "bit", "unit": None, "bit_position": 3,
     "description": "Critical Flag minimal bat #1 temperature: "},
    {"field": "critical_flag_over_temp", "size": 1, "type": "bit", "unit": None, "bit_position": 4,
     "description": "Critical Flag over temperature: "},
    {"field": "critical_flag_fault", "size": 1, "type": "bit", "unit": None, "bit_position": 5,
     "description": "Critical Flag EPS fault: "},
    {"field": "critical_flag_low_voltage", "size": 1, "type": "bit", "unit": None, "bit_position": 6,
     "description": "Critical Flag low voltage: "},
    {"field": "critical_flag_power_cycle", "size": 1, "type": "bit", "unit": None, "bit_position": 7,
     "description": "Critical Flag power cycle: "},
    {"field": "eps_temp_subsystem", "size": 8, "type": "int", "unit": "deg C",
     "description": "EPS subsystem temperature (degrees Celsius): "},
    {"field": "eps_hk_boot_count", "size": 8, "type": "uint", "unit": None,
     "description": "EPS MCU reboot count: "},

    # ********************************** ADCS *************************************
    {"group_name": "ADCS"},
    {"field": "mag1_field_x", "size": 16, "type": "int", "unit": "uT",
     "description": "X axis magnetic field component (magnetometer #1) value (uT): "},
    {"field": "mag1_field_y", "size": 16, "type": "int", "unit": "uT",
     "description": "Y axis magnetic field component (magnetometer #1) value (uT): "},
    {"field": "mag1_field_z", "size": 16, "type": "int", "unit": "uT",
     "description": "Z axis magnetic field component (magnetometer #1) value (uT): "},
    {"field": "mag2_field_x", "size": 16, "type": "int", "unit": "uT",
     "description": "X axis magnetic field component (magnetometer #2) value (uT): "},
    {"field": "mag2_field_y", "size": 16, "type": "int", "unit": "uT",
     "description": "Y axis magnetic field component (magnetometer #2) value (uT): "},
    {"field": "mag2_field_z", "size": 16, "type": "int", "unit": "uT",
     "description": "Z axis magnetic field component (magnetometer #2) value (uT): "},
    {"field": "accelero_x", "size": 16, "type": "int", "unit": "m/s^2", "description": "X axis acceleration (m/s^2): "},
    {"field": "accelero_y", "size": 16, "type": "int", "unit": "m/s^2", "description": "Y axis acceleration (m/s^2): "},
    {"field": "accelero_z", "size": 16, "type": "int", "unit": "m/s^2", "description": "Z axis acceleration (m/s^2): "},
    {"field": "gyro_x", "size": 16, "type": "int", "unit": "deg/s",
     "description": "Angular velocity on X axis (deg/s): "},
    {"field": "gyro_y", "size": 16, "type": "int", "unit": "deg/s",
     "description": "Angular velocity on Y axis (deg/s): "},
    {"field": "gyro_z", "size": 16, "type": "int", "unit": "deg/s",
     "description": "Angular velocity on Z axis (deg/s): "},
    {"field": "imtq_x", "size": 8, "type": "int", "unit": None, "description": "MTQ on X axis current: "},
    {"field": "imtq_y", "size": 8, "type": "int", "unit": None, "description": "MTQ on Y axis current: "},
    {"field": "imtq_z", "size": 8, "type": "int", "unit": None, "description": "MTQ on Z axis current: "},

    # *************************************** Camera ***********************************
    {"group_name": "Camera"},
    {"field": "shots_number", "size": 16, "type": "uint", "unit": None, "description": "Number of taken photos: "},
    {"field": "resolution", "size": 8, "type": "char", "unit": None, "description": "Resolution: ",
     "choice": [('1', '80 x 60'), ('2', '160 x 120'), ('3', '128 x 128'), ('4', '128 x 96'), ('5', '160 x 128'),
                ('6', '320 x 240'), ('7', '640 x 480')]},
    {"field": "image_type", "size": 8, "type": "char", "unit": None, "description": "Image Type: ",
     "choice": [('R', "Raw"), ('J', "JPEG")]},
    {"field": "reset_count", "size": 8, "type": "uint", "unit": None, "description": "Camera reset count: "},
    {"field": "camera_state", "size": 8, "type": "char", "unit": None, "description": "Camera State: ",
     "choice": [('0', "OFF"), ('1', "ON"), ('I', "Internal error."), ('C', "Comm error."),
                ('P', "Power error.")]},
]


class Parser:
    def __init__(self, endianness, **kwargs):

        self.endianness = endianness
        if 'database' in kwargs:
            self.database_name = kwargs['database']
            self.host = kwargs['host']
            self.user = kwargs['user']
            self.passwd = kwargs['passwd']
            self.database = None
            self.log_into_db()
        else:
            self.database_name = None
            self.host = None
            self.user = None
            self.passwd = None

        self.decoded_line = []
        self.decoded_data = []
        self.data_index = 0
        self.subsystem = None
        self.structure = None
        self.structure_length = None
        self.database_table = None
        self.orbit = None
        self.structured_data = None
        self.postfixes = []

    def setup_database(self, **kwargs):
        self.database_name = kwargs['database']
        self.host = kwargs['host']
        self.user = kwargs['user']
        self.passwd = kwargs['passwd']
        self.database = None
        self.log_into_db()

    def set_variables_and_parse(self, path, filename):
        self.subsystem = filename.split("_")[0]
        structure_object = TelemetryStructure(self.subsystem)
        self.structure, self.structure_length = structure_object.get_structure()
        self.database_table = "`" + self.subsystem + "`"
        self.orbit = filename.split("_")[1]
        self.add_record('Orbit', self.orbit)
        self.structured_data = self.define_structures(self.load_info(path + filename), self.structure_length)
        self.__universal_parser(self.structured_data)

    def add_record(self, name, value):
        postfix = ''
        if len(self.postfixes) > 0:
            for x in reversed(self.postfixes):
                postfix += x
        self.decoded_line.append({
            'field': name + postfix,
            'value': value
        })

    def close_data_line(self):
        self.decoded_data.append(self.decoded_line)
        self.decoded_line = []
        self.add_record('Orbit', self.orbit)

    def return_data(self):
        if len(self.decoded_data) > 0:
            return self.decoded_data

    @staticmethod
    def get_flag_value(full_byte, position):
        if ((full_byte >> position) & 0b1) == 1:
            return True
        else:
            return False

    @staticmethod
    def extract_unaligned_value(flags, byte_mask):
        value = flags & byte_mask
        while bool(byte_mask & 0b1) is False:
            value = value >> 1
            byte_mask = byte_mask >> 1
        return value

    def process_structure(self, y, structure, postfix=None):
        flags = None
        if postfix is not None:
            self.postfixes.append(postfix)
        for x in structure:
            value = None
            if x['field'] == 'flags_union':
                flags = self.combine_bytes(y[self.data_index: self.data_index + x['size']], type_of_val=x['type'])
                self.data_index += x['size']
            if x['type'] == 'struct':
                for end in x['multiplier']:
                    # Call this function recursively
                    self.process_structure(y, x['var'], end)
                    self.postfixes.pop(-1)
            elif x['type'] != 'struct' and type(x['size']) is tuple:
                value = []
                for z in x['size']:
                    if z == 1:
                        value.append(y[self.data_index])
                    else:
                        value.append(self.combine_bytes(y[self.data_index: self.data_index + z], type_of_val=x['type']))
                    self.data_index += z
            else:
                if x['field'] != 'flags_union':
                    if 'ignore' not in x.keys():
                        if x['size'] == 1:
                            value = y[self.data_index]
                            self.data_index += x['size']
                        elif x['size'] == 0:
                            if 'byte_mask' in x.keys():
                                value = self.extract_unaligned_value(flags, x['byte_mask'])
                            else:
                                value = self.get_flag_value(flags, x['bit_position'])
                        else:
                            value = self.combine_bytes(y[self.data_index: self.data_index + x['size']],
                                                       type_of_val=x['type'])
                            self.data_index += x['size']
                    else:
                        self.data_index += x['size']

            if value is not None:
                self.add_record(x['field'], value)

    def __universal_parser(self, data):
        for y in data:
            self.data_index = 0
            self.process_structure(y, self.structure)
            self.close_data_line()

    def log_into_db(self,):
        if self.database_name is not None:
            self.database = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.database_name
            )
        else:
            print("You didn't specify a database")

    @staticmethod
    def get_fields(data_line):
        fields = '`ID`'
        for data in data_line:
            fields += ', `' + data['field'] + "`"
        # print(fields)
        return fields

    @staticmethod
    def get_val_placeholders(data_line):
        placeholders = 'NULL'
        for _ in data_line:
            placeholders += ", %s"
        # print(placeholders)
        return placeholders

    @staticmethod
    def get_values(data_line):
        import datetime
        values = []
        for x in data_line:
            if 'timestamp' not in x['field']:
                values.append(str(x['value']))
            else:
                values.append(datetime.datetime.fromtimestamp(x['value']).strftime('%Y-%m-%d %H:%M:%S'))
        # print(values)
        return tuple(values)

    def send_data_to_database(self):
        import traceback
        try:
            if self.database is not None:
                for data_line in self.decoded_data:
                    cursor = self.database.cursor()
                    command = "INSERT INTO " + self.database_table + "(" + self.get_fields(data_line) + ") VALUES (" \
                              + self.get_val_placeholders(data_line) + ")"
                    cursor.execute(command, self.get_values(data_line))
                    self.database.commit()
            else:
                return 'You are not logged into any database. Please use function log_into_db.'
        except Exception as e:
            traceback.print_exc()
            print('Error sending to db: \n')
            print(e)

        self.decoded_data = []
        self.decoded_line = []

    @staticmethod
    def load_info(path):
        data = np.fromfile(path, dtype=np.uint8)
        return data

    @staticmethod
    def define_structures(data, size):
        if data is not None:
            if len(data) % size != 0:
                print('Incomplete data. The file was truncated.')
            while len(data) % size != 0:
                data = np.delete(data, -1)
            return np.reshape(data, (-1, size))
        else:
            raise ValueError('No data.')

    def combine_bytes(self, value, endianness=None, type_of_val=None):
        if endianness is None:
            endianness = self.endianness

        def check_sign_bit(val):
            if ((val >> 7) & 0b00000001) == 1:
                return -1
            else:
                return 1

        if endianness == 'little':
            value = np.flipud(value)
        result = 0

        if type_of_val == 'uint':
            sign = 1
            insufficient_bit = 0
        else:
            try:
                sign = check_sign_bit(value[0])
            except IndexError as e:
                sign = 1
                print('Error getting the sign bit. It will be defaulted as +.')
                print(e)
            if sign == -1:
                insufficient_bit = 1
                value = [~x for x in value]
            else:
                insufficient_bit = 0

        for x in value:
            result = (result << 8) + x

        return (result + insufficient_bit) * sign



class Decoder:
    def __init__(self, standalone=False):
        self.standalone = standalone
        parser = Parser(endianness='little')
        self.combine_bytes = parser.combine_bytes
        self.tlm_struct = []
        self.db_log = False
        self.database = []

    def set_db_logging(self, state: 'bool'):
        self.db_log = state

    @staticmethod
    def check_for_13(msg: 'np.ndarray') -> 'np.ndarray':
        replacement = np.uint8(13)
        length = len(msg)
        msg = np.copy(msg)
        correction_bytes = [-4, -3, -2, -1]
        for i in correction_bytes:
            if msg[i] > np.uint8(97):
                print(f'Error, the invalid character position is out of boundaries can not compensate the error.')
                return msg
            elif msg[i] != np.uint8(0):
                msg[msg[i] - length] = replacement
            else:
                return msg
        return msg

    def decoder(self, msg: 'np.ndarray'):
        pos = 0
        result = None
        result_text = ''

        msg = self.check_for_13(msg)

        for i in packet:
            if self.standalone:
                if 'group_name' in i:
                    line = f'<<{i["group_name"]:*^66}>>'
                    print(line)
                elif 'sub_group_name' in i:
                    line = f'{i["sub_group_name"]:-^70}'
                    print(line)
                if 'type' in i:
                    if i['type'] == 'char':
                        if 'choice' in i:
                            try:
                                cut = chr(msg[pos])
                            except IndexError:
                                if self.standalone:
                                    print(f'Index out of boundaries.')
                                cut = None
                            pos += i['size'] // 8

                            for var in i['choice']:
                                if var[0] == cut:
                                    result = var[1]
                                    break
                                else:
                                    result = f'Decoder error. Could not decode the received byte!'
                        else:
                            cut = msg[pos:pos + i['size'] // 8]
                            for j in cut:
                                result_text += chr(j)
                            pos += i['size'] // 8
                    elif i['type'] == 'uint' or i['type'] == 'int':
                        result = self.combine_bytes(value=msg[pos: pos + i['size'] // 8], type_of_val=i['type'])
                        pos += i['size'] // 8
                    elif i['type'] == 'bit':
                        if i['size'] == 1:
                            try:
                                result = bool((msg[pos] >> (7 - i['bit_position'])) & 1)
                            except IndexError:
                                if self.standalone:
                                    print(f'Index out of range.')
                        if i['bit_position'] + i['size'] > 7:
                            pos += 1

                    if result is not None:
                        if 'conversion' in i:
                            if self.standalone:
                                print(f'{i["description"]}{str(i["conversion"](result))}')
                            if self.db_log and 'unit' in i:
                                self.database.append(i['conversion'](result))
                            self.tlm_struct.append({'field_name': i['field'], 'value': i['conversion'](result)})
                        else:
                            if self.standalone:
                                try:
                                    print(f'{i["description"]}{str(result)}')
                                except KeyError:
                                    print("No description found fo this field.")
                            if self.db_log and 'unit' in i:
                                self.database.append(result)
                            self.tlm_struct.append({'field_name': i['field'], 'value': result})
                    elif result_text != '':
                        if self.standalone:
                            try:
                                print(f'{i["description"]}{result_text}')
                            except KeyError:
                                print("No description found fo this field.")
                        if self.db_log and 'unit' in i:
                            self.database.append(result_text)
                        self.tlm_struct.append({'field_name': i['field'], 'value': result_text})
            else:
                if 'type' in i:
                    if i['type'] == 'char':
                        if 'choice' in i:
                            try:
                                cut = chr(msg[pos])
                            except IndexError:
                                if self.standalone:
                                    print(f'Index out of boundaries.')
                                cut = None
                            pos += i['size'] // 8

                            for var in i['choice']:
                                if var[0] == cut:
                                    result = var[1]
                                    break
                                else:
                                    result = f'Decoder error. Could not decode the received byte!'
                        else:
                            cut = msg[pos:pos + i['size'] // 8]
                            for j in cut:
                                result_text += chr(j)
                            pos += i['size'] // 8
                    elif i['type'] == 'uint' or i['type'] == 'int':
                        result = self.combine_bytes(value=msg[pos: pos + i['size'] // 8], type_of_val=i['type'])
                        pos += i['size'] // 8
                    elif i['type'] == 'bit':
                        if i['size'] == 1:
                            try:
                                result = bool((msg[pos] >> (7 - i['bit_position'])) & 1)
                            except IndexError:
                                if self.standalone:
                                    print(f'Index out of range.')
                        if i['bit_position'] + i['size'] > 7:
                            pos += 1

                    if result is not None:
                        if 'conversion' in i:
                            if self.standalone:
                                print(f'{i["description"]}{str(i["conversion"](result))}')
                            if self.db_log and 'unit' in i:
                                self.database.append(i['conversion'](result))
                            self.tlm_struct.append({'field_name': i['field'], 'value': i['conversion'](result)})
                        else:
                            if self.standalone:
                                print(f'{i["description"]}{str(result)}')
                            if self.db_log and 'unit' in i:
                                self.database.append(result)
                            self.tlm_struct.append({'field_name': i['field'], 'value': result})
                    elif result_text != '':
                        if self.standalone:
                            print(f'{i["description"]}{result_text}')
                        if self.db_log and 'unit' in i:
                            self.database.append(result_text)
                        self.tlm_struct.append({'field_name': i['field'], 'value': result_text})

    def get_json(self):
        import json
        # Make sure that all the data in the database if of python base classes. Convert if it is of numpy classes.
        for i in range(len(self.database)):
            if type(self.database[i]) is np.int64:
                self.database[i] = int(self.database[i])
            elif type(self.database[i]) is np.float64:
                self.database[i] = float(self.database[i])

        result = json.dumps(self.database)
        del self.database[:]
        return result

    def get_telemetry(self, message):

        def strip_callsign(msg: 'np.ndarray') -> 'tuple[np.ndarray, str]':
            callsign = ''
            for i in range(0, 6):
                callsign += chr(msg[i] >> 1)
            # The byte in position 6 is the SSID of the Destination which is why we ignore it
            msg = msg[7:]
            return msg, callsign

        self.tlm_struct = []
        self.database = []

        t = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
        self.tlm_struct.append({'field_name': 'tlm_date_time', 'value': int(time.time())})
        message, dst_callsign = strip_callsign(message)
        self.tlm_struct.append({'field_name': 'dst_clsgn', 'value': dst_callsign})
        message, src_callsign = strip_callsign(message)
        self.tlm_struct.append({'field_name': 'src_clsgn', 'value': src_callsign})
        if self.standalone:
            line = f'{"TUMnanoSAT Telemetry":#^70}\n{current_time: ^70}\nDestination callsign: {dst_callsign}\n' \
                   f'Source callsign: {src_callsign}'
            print(line)
        # Now that we truncated the Source and destination callsign, we are left with the rest of the message.
        # After Source callsign there is a Control field byte and an SSID byte which we also need to cut out
        message = message[2:]
        self.decoder(message)
        return self.tlm_struct
    
def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def main():
    decoder = Decoder(standalone=True)
    message=input()
    message=message.replace(' ','')
    message=bin(int(message, 16))[2:].zfill(8)
    message= bitstring_to_bytes(message)
    message=np.frombuffer(message, dtype=np.uint8)
    decoder.get_telemetry(message)
    

if __name__ == '__main__':
    main()
