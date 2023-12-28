# LeavesDetection
 A YoloV8-based tree leaf detection module.

### **Required - pretrained (.pt) files**
Because of GitHub's 100MB file limit, YoloV8's *.pt* files cannot be uploaded to this repository. **Required files are available [here](https://drive.google.com/file/d/1Vj1OTCirn1xH_4zl5NX2p0Q2V1oHJvXE/view?usp=sharing).**

Unzip them and move the contents into the main catalogue in order for this model to work, or pretrain your own model using train.py and selected YoloV8 module.

**This model's MARPE score is 3.27.**

### Concept
This model has been pretrainted to detect leaves of 5 distinct trees - aspen, birch, gazel, maple and oak.

![LeavesDetectionExample](https://github.com/Marcin-Galaska/LeavesDetection/assets/106023363/fb331b66-9053-4924-a0bf-759594a88c02)

### Usage

**Do remember to unpack .pt files in the main catalogue or pretrain the model yourself before attempting to use real-time detection.**

Required Python packages are described in the requirements.txt file.

Model training is performed through the tran.py file.

Real-time leaf detection is performed through the detect.py file. 

Training and validating images can be found in the datasets folder.

The results of training on YoloV8m and YoloV8x can be found in the runs folder.

### License
BSD 2-Clause License

Copyright (c) 2023, Marcin Gałąska <br>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
