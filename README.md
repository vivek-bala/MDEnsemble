MDEnsemble API
============

Provides an easy-to-use interface based on BigJobAsync and provides functional support to execute Molecular Dynamics simulations 


Requirements
============

* Python >= 2.5
* BigJobAsync 0.2

BigJobAsync Installation
========================

To install BigJobAsync follow the instructions on 

```bash
https://github.com/oleweidner/BigJobAsync/
```

Adding a Resource
==================

The resource dictionary is a set of configurations for different possible resources that might be used. 
```bash
https://github.com/oleweidner/BigJobAsync/blob/master/bigjobasync/resource_dictionary.py
```

The resources are referenced through the config.py file.

To use a new resource, it is enough to add the details of the resource to the resource_dictionary.py file.


Configuration file
==================

This is the primary configuration file that needs to modified by the user.
```bash
https://bitbucket.org/vivek-balasubramanian/mdensembleapi/src/f0f6d5c6eccd51c94a0db422d1d88b3780e799aa/gromacs_bjasync/config.py?at=master
```

Two set of details to be filled in - RESOURCE details and TASK details.

RESOURCE DETAILS (example):-


		'remote_host' : 'FUTUREGRID.SIERRA',
		'remote_directory' : '/N/u/vivek91/tryout/',
		'username' : 'vivek91',
		'number_of_cores' : 2,
		'resource_name' : "sierra:12cores",
		'project_id' : "TG-MCB090174",
		'walltime' : 10

remote_host -  The target host where resource is to be acquired

remote_directory - Working directory in the remote host

username - Username required to login to the remote host

number_of_cores - Number of cores to be acquired at the remote host for all the tasks

resource_name - User can name the resource for identification purposes incase of multiple resource acquisitions at the same remote host

project_id - User can name the project for identification purposes

walltime - Time in minutes for which the resources are to be acquired


TASK DETAILS (example):-



		'source_directory' : '/home/vivek/Research/Gromacs/',
		'output_directory' : ".",

		'pdbfile' : 'aladip.pdb',
		'emfile' : 'em.mdp',
		'runfile' : 'run.mdp',
		'app_kernel' : 'gromacs_python_wrapper.py',
		
		'cores_per_task' : 1,
		'number_of_tasks' : 2,
	
		'force_field' : '"amber03"',
		'water_model' : 'none'


source_directory - Path at localhost from where files need to be transferred

output_directory - Path at localhost where output files need to be transferred

pdbfile,emfile,runfile - Input filenames for the ensemble member

app_kernel_ - Filename of the python wrapper(placed in the gromacs_bjasync folder)

cores_per_task - Number of cores to be allocated to eack task

number_of_tasks - Number of ensemble members

force_field, water_model - Input parameters for the ensemble



Running the example
===================

Running the example is quite simple. Most of the changes have to be made in the config file and the file to be executed 
remains the same.

```bash
python example.py
```


