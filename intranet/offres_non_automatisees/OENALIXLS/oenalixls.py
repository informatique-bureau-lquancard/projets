import xlrd
import xlwt
import csv
import glob
import re
import io
import time
import sys
from unidecode import unidecode

reader = xlrd.open_workbook('*.xlsx')
