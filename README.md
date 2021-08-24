# w_crawl augmentation

Code to augment a west.h5 file with coordinates from trajectories.

Most of the `crawl.py` code is directly adapted from the w_crawl example at https://github.com/westpa/westpa/wiki/man:w_crawl .


## Setup

A few system-specific paths need to be provided to each script.

### `crawl.py`

Change:
- `base_sim_path` to the root WESTPA sim folder
- `topology_filename` to point to a topology file for your system
- `child_traj_pattern` and `parent_traj_pattern` to point to the child/parent trajectories for each iteration.

### `augment.py`

Change:
- `source_h5` to point to the root west.h5 file.

## Running

1. Run ` w_crawl crawl.calculate  -c crawl.crawler -W <path_to_west_h5>`

    This will go through each iteration and store 2 frames of coordinates (parent/child) 
     for each in `augment_data.h5`.
   
    If no trajectory file exists, it just puts NaNs in for the coordinates.
   
2. Run `python augment.py`

    This will copy all the coordinates from `augment_data.h5` into `iter_XXXX/auxdata/coord` of the main H5
   file.
   
