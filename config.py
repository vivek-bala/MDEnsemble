#!/usr/bin/env python

# ----------------------------------------------------------------------------
# MAIN DESCRIPTION

RESOURCE = {
		#Resource related inputs	--MANDATORY
		'remote_host' : 'FUTUREGRID.SIERRA',
		'remote_directory' : '/N/u/vivek91/tryout/',
		'username' : 'vivek91',
		'number_of_cores' : 2,
		'resource_name' : "sierra:12cores",
		'project_id' : "TG-MCB090174",
		'walltime' : 10
	}
	
TASK = {
		#Task related inputs		--MANDATORY
		
		#Paths/Directories involved
		'source_directory' : '/home/vivek/Research/EnsembleAPI/gromacs_input_alanine_dipeptide/',
		'output_directory' : "",

		#input + kernel names
		'pdbfile' : 'aladip.pdb',
		'emfile' : 'em.mdp',
		'runfile' : 'run.mdp',
		'app_kernel' : 'gromacs_python_wrapper.py',
		
		#Resource requirement and number of tasks
		'cores_per_task' : 1,
		'number_of_tasks' : 2,
	
		#Ensemble Parameters
		'force_field' : '"amber03"',
		'water_model' : 'none'
	}
    
