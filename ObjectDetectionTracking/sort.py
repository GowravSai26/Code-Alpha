# SORT tracker implementation (clean version)
import numpy as np
from filterpy.kalman import KalmanFilter
from scipy.optimize import linear_sum_assignment

class KalmanBoxTracker:
    count = 0
    def __init__(self, bbox):
        self.kf = KalmanFilter(dim_x=7, dim_z=4)
        self.kf.F = np.array([[1,0,0,0,1,0,0],
                              [0,1,0,0,0,1,0],
                              [0,0,1,0,0,0,1],
                              [0,0,0,1,0,0,0],
                              [0,0,0,0,1,0,0],
                              [0,0,0,0,0,1,0],
                              [0,0,0,0,0,0,1]])
        self.kf.H = np.array([[1,0,0,0,0,0,0],
                              [0,1,0,0,0,0,0],
                              [0,0,1,0,0,0,0],
                              [0,0,0,1,0,0,0]])

        self.kf.x[:4] = bbox.reshape((4,1))
        self.time_since_update = 0
        self.id = KalmanBoxTracker.count
        KalmanBoxTracker.count += 1

    def update(self, bbox):
        self.kf.update(bbox)

    def predict(self):
        self.kf.predict()
        return self.kf.x[:4]

class Sort:
    def __init__(self):
        self.trackers = []

    def update(self, detections):
        updated = []
        for det in detections:
            matched = False
            for trk in self.trackers:
                trk.update(det)
                matched = True
                break
            if not matched:
                self.trackers.append(KalmanBoxTracker(det))
        for trk in self.trackers:
            updated.append((trk.predict().flatten(), trk.id))
        return updated
