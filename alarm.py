# =====================================================
# ALARM SYSTEM
# =====================================================
#
# Amaç:
# Hareket veya insan algılanınca sesli uyarı vermek
#
# =====================================================

import winsound  # Windows için ses

class AlarmSystem:

    def __init__(self):

        print("Alarm sistemi aktif.")

    def trigger(self):

        # beep sesi
        winsound.Beep(1000, 500)

        print("!!! ALARM: ŞÜPHELİ DURUM ALGILANDI !!!")
