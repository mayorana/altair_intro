# Intro to Altair 

## 1. Setup

1. Create the environment
```conda env create -f requirements.yml```
2. Register the kernel with jupyter
```python -m ipykernel install --user --name=altair_intro```
3. Make sure you are authenticated with `glcoud auth` (`gcloud auth application-default login`). If you don't have google cloud authentication set up, you can skip this part and download the data manually as described in the notebook.
3. Now you should be able to run the notebook `altair_intro.ipynb`.