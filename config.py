MAX_WORKERS = 30
MAX_WORKERS = 30
FOLDER_PATH = 'liver_data'  # Mettez à jour le chemin vers le dossier contenant les données de foie
GRAPH_PATH = 'liver_graphs'  # Mettez à jour le chemin vers le dossier où vous souhaitez enregistrer les graphes
SAVED_MODEL_PATH = 'saved_models'  # Mettez à jour le chemin vers le dossier où vous souhaitez enregistrer les modèles entraînés
SAVED_DATA_LOADER = 'saved_data_loader'  # Mettez à jour le chemin vers le dossier où vous souhaitez enregistrer les dataloaders prétraités

feature_size = {
    "resnet18": 512,  # Mettez à jour la taille des caractéristiques si nécessaire
    "densenet121": 1024,  # Mettez à jour la taille des caractéristiques si nécessaire
    "efficientnet-b0": 1280  # Mettez à jour la taille des caractéristiques si nécessaire
}


saved_data_loader = {'test_dataloader_150_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1h2kHFklOw9j5Lu7sxz7SekLtFbMJPw25',
 'val_dataloader_150_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1aLe5bxC6aHQiA-LRMznidBll8q3vJIVq',
 'train_dataloader_150_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1EN4M5_I-DlAQPrTLx4rZoG6ioAhPuXfE',
 'test_dataloader_300_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1xh_ct7RXg97D1-aN0p8n5H4RnL6X_3YV',
 'val_dataloader_300_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1puV6XzFj0WEMq8P9EJCrJQpWCTaRO0EB',
 'train_dataloader_300_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1I-8Bqo1SFKD_c3NpZYyjL8pdLa_RHq_y',
 'test_dataloader_300_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1rmHZdlBifY2KCz-Q0VcOLlqppM-6hZ2b',
 'val_dataloader_300_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1afTGdQxH8_wdotXyMv-Zy62gvVGKNUX8',
 'train_dataloader_300_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1lOoibzD112n-iH_uAbGTgSDnaZ0d6iit',
 'val_dataloader_300_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1cfrdwTHRDDWBlT1L4b1XPupzTG7GCcsU',
 'test_dataloader_300_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1NO5kh4eCKZBc1GIYKAupEQTNw5cBpo4z',
 'train_dataloader_300_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1iKZfo14Y3PbqRG2Ug0eDQgqU2-zvFzj4',
 'test_dataloader_150_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1XQCysYDx2rDDFmWdruneQcqeDi1qE2r_',
 'val_dataloader_150_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1wL8iCyu8wIt0si_S2AB1UKhee2yNZMfc',
 'train_dataloader_150_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1R0S9uK6Bw-8pcv0V65cNB2DZp_Isq94y',
 'val_dataloader_150_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1c5xBoz7Ys8LfC_BhLeak4WpJJxa9w-74',
 'test_dataloader_150_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1K4nagfijNzJZpS5opXLp0ECyKJcrNf8D',
 'train_dataloader_150_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=18rQ5JK5DwQH3plxFCmMVXQR-K7HfBYy_',
 'test_dataloader_100_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1fZEZ3meX-5YoQgSM9XfxKUgJSYHrPD9d',
 'val_dataloader_100_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1MUONtYfXIk2q6gfW1Ql64Wbdr50hQJud',
 'train_dataloader_100_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1rZWQajlHbf2YWy1rMljdAU0srX0pj9u8',
 'val_dataloader_100_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1R8YT9UbpzxiIDJlcr5KbECBfGb-AjC9_',
 'test_dataloader_100_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1Xcpjsx5Xh9ADykaiBJtjuQDex1yRQk6k',
 'train_dataloader_100_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=10Zi_Euqp0lil_LXQ0YcHBNOP7C6NlHm9',
 'test_dataloader_100_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1N9UsaNavKK-E0cwNEZKsop1cITj9NHKR',
 'val_dataloader_100_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1tyx96xNloNRrQ4BnUGtSV5ohosKemaDt',
 'train_dataloader_100_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1wEU83lI-ZHUqzlTIkQsuuGAc1f63JirJ',
 'train_dataloader_50_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1fPiKs8VokWvipU9KmqzIsD37GZ4mIcCg',
 'test_dataloader_50_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1LZKew9P6Saw_bDNBBZggXUXt6NQ9GoY3',
 'val_dataloader_50_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1uj3qMWLdZn5sgOusCWXsDYWv2blKgJeF',
 'train_dataloader_50_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1egDlFd3LGRei7ZH7eivlzJvKTlBXocco',
 'val_dataloader_50_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1gupnjP9h6ZyHpF6oeKIjX0gYF9S1oIaR',
 'test_dataloader_50_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1l965cHr03OprP-CqPleSAjeGhb0aFI2Z',
 'train_dataloader_50_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=131C6w--aioNANoKxiSzTpKmlDZxPzPYk',
 'val_dataloader_50_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=147DYPUQ1-ptdFekSGHZ8zWWMUZtaGTkT',
 'test_dataloader_50_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1gotP7vfQ_ItiE6Re_rUC4642aupavpgq',
 'test_dataloader_10_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1o--zMfPsSNJkPcnBfRqVlXrpbuw3lKmB',
 'train_dataloader_10_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=17j32kG-LCe8VaiRASRCx-lmLyBVzA2Uz',
 'val_dataloader_10_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=14tLZ-wadnYBYCRJtQrIOHCoD9QTI4jQH',
 'test_dataloader_10_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1MtAOjEQ8yYftcmGE0QbKF7yWQQ86VIdq',
 'val_dataloader_10_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1nadHIRlTLthi1QPK3u29H96V2kiDzMaq',
 'train_dataloader_10_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1TNVitz47TFxzCe5Z4jAoGMVoJxwz_Edw',
 'test_dataloader_10_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=10jqaBy58RC4L1XotVBgKs4ww8bE_NtJh',
 'val_dataloader_10_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1WYWz9OC_ESrnJxSUWM-M6ML4EcqmVRk0',
 'train_dataloader_10_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1ET_Mp0tROoXJ2ICvSTYtgohE2d6rU9Ko',
 'test_dataloader_5_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1PQUHzYgq53_zvC7Ma1iIDqYaMy6lasDx',
 'val_dataloader_5_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1g64rLLcqhzZjQ3wczfDBvrOqkPasA23G',
 'train_dataloader_5_resnet18': 'https://drive.google.com/uc?export=download&confirm=yes&id=1cemz-GIWMBY30mDF16a0AG3sFZPRPwOR',
 'test_dataloader_5_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1ouBkOedYRXp3t7-S8bwx1c1loLuKdUsX',
 'val_dataloader_5_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1zlNY-o24Q8SBAjYz5yqPoqiu38d-nYLx',
 'train_dataloader_5_efficientnet-b0': 'https://drive.google.com/uc?export=download&confirm=yes&id=1CSFOHmykQzipVs4CW4cs0Yl9IOPqvMaT',
 'train_dataloader_5_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1zXYwgT_ZjepQOqBfI6iGfY1PCrJhvGhD',
 'val_dataloader_5_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1fN4FpnexOT9vb1X4139go7s5MsAnTSE5',
 'test_dataloader_5_densenet121': 'https://drive.google.com/uc?export=download&confirm=yes&id=1oZAyAv72R919Tx2IqgeBshAcMDirkiX6'}
