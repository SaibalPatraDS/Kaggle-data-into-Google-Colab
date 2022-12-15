from google.colab import files
files.upload() 
'''upload your kaggle.json file now'''

!rm -r ~/.kaggle
!mkdir ~/.kaggle
!mv ./kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets list

! kaggle competitions download -c 'name of competition'

!unzip "file_name.zip"
