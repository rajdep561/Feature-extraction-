import os

# Set a single environment variable
#os.environ['MY_VARIABLE'] = 'my_value'

# Set multiple environment variables
os.environ.update({
    'FDCT': '/home/rajdeep/projects/Feature-extraction-/data/FDCT',
    'FFTW': '/home/rajdeep/projects/Feature-extraction-/data/FFTW'})
