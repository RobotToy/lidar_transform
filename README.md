# lidar_transform

Lidar stabilization and 3D lidar to 2D image projections

References the following links:
- https://medium.com/swlh/camera-lidar-projection-navigating-between-2d-and-3d-911c78167a94
- https://github.com/darylclimb/cvml_project/tree/cb06850b9477550b9c9e3c5651d013b347cc9b1b
- https://docs.google.com/document/d/1RjBsUXEFKcb9vYRMPgeQT-MpWPQjjVro7LR12HOLSQQ/edit?usp=sharing

Updated from Referenced Github to work with the following dependencies:
- Ubuntu 22.04
- ROS Humble
- Anaconda Python 3.7

Step 1
- Clone Github to chosen workspace

Step 2:
- Install Conda/Miniconda (to model local setup, use miniconda)
  - Download Installer:
    - https://conda.io/projects/conda/en/stable/user-guide/install/linux.html
    - <img width="502" alt="image" src="https://github.com/RobotToy/lidar_transforms/assets/44909129/cee866b2-c602-416e-adb9-63deb862aff9">

  - Verify Installer Hashes:
    -   https://conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification
    -   https://docs.anaconda.com/free/anaconda/reference/hashes/all/
    - SHA-256 Checksums: `sha256sum filename`
      - Ex: `sha256sum ~/Downlaods/Anaconda3-2023.07-0-Linuz-x86_64.sh
`
  -   Download Bash
    `bash Anaconda-latest-Linux-x86_64.sh`
      - Ex: `bash ~/Downloads/Anaconda3-2023.07-0-Linux-x86_64.sh`
  - Accept, verify install location, and install

Step 3: Create Conda Environment
- `conda create -name <name_of_workspace> python=3.7`
- Answer y to prompt

Step 4: Activate Conda Environment
- `conda activate <name_of_workspace>`
- Answer y to prompt

Step 5: Install Requirements File
- `pip3 install -r requirement.txt`
- *** May need to edit requirement file
  - Edit file so it looks like the following:
  - <img width="466" alt="image" src="https://github.com/RobotToy/lidar_transforms/assets/44909129/c9f009c2-e6be-4035-89c3-acf0b96cfc37">

Step 6: Install Remaining Dependencies
- i.e. `conda install -c anaconda mayavi`
- Additional dependencies that may need to be installed:
  - https://anaconda.org/anaconda/pandas
  - https://anaconda.org/conda-forge/plyfile
  - https://anaconda.org/conda-forge/tqdm https://anaconda.org/anaconda/scikit-learn
  - https://anaconda.org/anaconda/mayavi
  - https://anaconda.org/conda-forge/vtk

Step 7: Run Py File
