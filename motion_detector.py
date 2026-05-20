# =====================================================
# MOTION DETECTOR
# =====================================================
#
# Amaç:
# İki frame arasındaki farkı bulup hareket algılamak
#
# Kullanılan konu:
# - image processing
# - numpy
# - class (OOP)
# =====================================================

import cv2
import numpy as np


class MotionDetector:

    # CONSTRUCTOR
    def __init__(self, threshold=25):

        # hareket hassasiyeti
        self.threshold = threshold

        # önceki frame
        self.previous_frame = None

        print("Motion Detector hazır.")

    # hareket algılama
    def detect(self, frame):

        # griye çevir (daha hızlı işlem)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # blur (gürültü azaltma)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # ilk frame ise kaydet
        if self.previous_frame is None:
            self.previous_frame = gray
            return False

        # fark al
        frame_diff = cv2.absdiff(self.previous_frame, gray)

        # threshold uygula
        _, thresh = cv2.threshold(frame_diff, self.threshold, 255, cv2.THRESH_BINARY)

        # değişim var mı kontrol et
        motion_score = np.sum(thresh)

        # güncelle
        self.previous_frame = gray

        # hareket varsa True döndür
        return motion_score > 10000
