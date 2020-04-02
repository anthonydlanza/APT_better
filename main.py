import autoline
from autoline import addLine
from autoline import *

line = autoline.line
tens = autoline.tens
tens_holder = autoline.tens_holder


gosub_goto = tens
pump_count = 8
local_begin = "LOCAL(SEQM,MAXSEQ,MAXTOT,SEQ,CHANGE)\n"
local_middle = "LOCAL("
local_middle2_ena = False
local_middle2 = "LOCAL("
local_middle3_ena = False
local_middle3 = "LOCAL("
local_end = "LOCAL("
local_reqs = "LOCAL(PLT,PDT,PDTMR,PUTMR,PEN)\n"
timers = "LOCAL("
totals = ""
sequences = ""
args = ""

for x in range(1,pump_count+1):
	if(x < 4):
		local_middle = local_middle + "P" + str(x) + "TOT,"  + "SEQ" + str(x) + ","
	elif(x >= 4):
		local_middle2_ena = True
		local_middle2 = local_middle2 + "P" + str(x) + "TOT,"  + "SEQ" + str(x) + ","
	local_end = local_end + "L" + str(x) + ","
	totals = totals + "$P" + str(x) + "TOT,"
	sequences = sequences + "$SEQ" + str(x) + " + "
	args = args + "$ARG" + str(x) + ","
	timers = timers + "P" + str(x) + "TMR,"

local_middle = local_middle[:-1] + ")"
local_middle2 = local_middle2[:-1] + ")"
args = args[:-1] + ")"

for x in range(10):
	print(f"{addLine()} C *")
print(f"{addLine()} {local_middle}")
if local_middle2_ena:
	print(f"{addLine()} {local_middle2}")