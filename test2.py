import biolib
import os
os.environ["BIOLIB_TOKEN"] = "0azDW0zI0bcjYSmmqh08uW1uf2htqkAVEWHGmmzvZb4"

biolib.login()

app_list = biolib.search('samtools')
print(app_list)

app = biolib.load(app_list[0])
job = app.cli('--help')

print(job.get_stdout())    # Returns stdout as bytes
print(job.get_stderr())   # Returns stderr as bytes
print(job.get_exit_code()) # Returns exit code of the application as an integer

# job.save_files(output_dir='.')
