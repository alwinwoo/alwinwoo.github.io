# How to use
# GOOGLE_COLAB = True
# GDRIVE_ROOT = '/content/drive/MyDrive/Colab Notebooks/1 Elyon/00 AI Websites/'
# mount_Google_drive(GOOGLE_COLAB, GDRIVE_ROOT)

def mount_Google_drive(GOOGLE_COLAB = True, GDRIVE_ROOT = '/content/drive/MyDrive/Colab Notebooks'):

  from pathlib import Path

  if GOOGLE_COLAB:

    if Path('/content/drive/MyDrive/Colab Notebooks/data/drive_online.txt').exists():
      print('Google Drive mounted.')
    else:
      try:
        from google.colab import drive
        drive.mount('/content/drive')
        Path('/content/drive/MyDrive/Colab Notebooks/data/drive_online.txt').touch()
        print('Google Drive mounted.')
      except:
        print('Error mounting Google Drive.')