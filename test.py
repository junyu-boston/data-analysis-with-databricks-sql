import biolib
import os
os.environ["BIOLIB_TOKEN"] = "0azDW0zI0bcjYSmmqh08uW1uf2htqkAVEWHGmmzvZb4"

biolib.login()

samtools = biolib.load('samtools/samtools')
job = samtools.cli(args='--help', blocking=False)
print(job.get_stdout().decode())
print(job.get_status())