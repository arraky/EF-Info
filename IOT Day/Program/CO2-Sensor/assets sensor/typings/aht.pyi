"""Driver for AHT2x sensors (humidity and temperature):
    Models: AHT20 and AHT21
    Adresse i2c: 56 (0x3b)
    Official website of the manufacturer: http://www.aosong.com
"""
from typing import Literal


class AHT2x:
    """Class based on AHT20 and AHT21 documentation."""

    def __init__(self, i2c, address=Literal, crc=False):
        """Parameters:
        i2c: instance of machine.I2C
        address: i2c address of sensor
        crc: Boolean for CRC control. True to active the CRC control."""


    @property
    def is_busy(self) -> bool:
        """The sensor is busy until the measurement is complete."""

    @property
    def is_calibrated(self) -> bool:
        """The activation of the calibration must be done before any
        measurement. If not, do a soft reset."""

    def _status(self):
        """The status byte initially returned from the sensor.
        Bit     Definition  Description
        [0:2]   Remained    Remained
        [3]     CAL Enable  0:Uncalibrated,1:Calibrated
        [4]     Remained    Remained
        [5:6]   Remained    Remained
        [7]     Busy        0:Free in dormant state, 1:Busy in measurement"""

    @property
    def humidity(self) -> float:
        """The measured relative humidity in percent."""

    @property
    def temperature(self) -> float:
        """The measured temperature in degrees Celsius."""

    @property
    def status(self) -> int:
        ...
    def reset(self):
        """The soft reset command is used to restart the sensor system without
        turning the power off and on again. After receiving this command, the
        sensor system begins to re-initialize and restore the default setting
        state"""

    def _calibrate(self):
        """Internal function to send initialization command.
        Note: The  calibration  status  check  in  the  first  step
            only  needs  to  be  checked  at  power-on.  No  operation is
            required during the normal acquisition process."""

    def _crc8(self):
        """Internal function to calcule the CRC-8-Dallas/Maxim of current
        message. The initial value of CRC is 0xFF, and the CRC8 check
        polynomial is: CRC [7:0] = 1+X^4 +X^5 +X^8"""


    def _measure(self):
        """Internal function for triggering the AHT to read temp/humidity"""