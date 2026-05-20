# =====================================================
# CAMERA MODULE
# =====================================================
#
# Amaç:
# Kamera işlemlerini ayrı sınıfa almak
#
# OOP prensibi:
# - separation of concerns
# =====================================================

import cv2


class Camera:

    def __init__(self, index=0):

        # kamera açılır
        self.cap = cv2.VideoCapture(index)

        print("Kamera başlatıldı.")

    def read_frame(self):

        # frame oku
        ret, frame = self.cap.read()

        return ret, frame

    def release(self):

        # kamera kapat
        self.cap.release()
