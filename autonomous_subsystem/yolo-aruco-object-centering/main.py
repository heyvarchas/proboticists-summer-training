import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")

aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

detector = cv2.aruco.ArucoDetector(
    aruco_dict
)

cap = cv2.VideoCapture(2)

while True:

    frame_x = None
    frame_y = None

    ret, frame = cap.read()

    if not ret:
        print("Camera read failed")
        break

    #Running YOLO on every frame, we're gonna target a water bottle for now
    results = model(frame, verbose=False)
    TARGET = "bottle"

    #After yolo inference, this part will check if the bottle is in the frame. If it isn't there, don't do anything.
    obj_x = None
    obj_y = None
    
    for box in results[0].boxes:
    
        cls = int(box.cls[0])
    
        name = model.names[cls]
    
        if name != TARGET:
            continue
    
        x1, y1, x2, y2 = box.xyxy[0]
    
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
    
        obj_x = (x1 + x2) // 2
        obj_y = (y1 + y2) // 2
    
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (255, 0, 0),
            2
        )
    
        cv2.circle(
            frame,
            (obj_x, obj_y),
            8,
            (255, 0, 0),
            -1
        )
    
        break
    
    corners, ids, _ = detector.detectMarkers(frame)

    if ids is not None:

        centers = {}

        for corner, marker_id in zip(
                corners,
                ids.flatten()
        ):
        
            pts = corner[0]
        
            cx = int(pts[:,0].mean())
            cy = int(pts[:,1].mean())
        
            centers[marker_id] = (cx, cy)
        
            cv2.circle(
                frame,
                (cx, cy),
                5,
                (0,255,0),
                -1
            )

        required = [0,1,2,3]

        if all(i in centers for i in required):
        
            frame_x = sum(
                centers[i][0]
                for i in required
            ) // 4
        
            frame_y = sum(
                centers[i][1]
                for i in required
            ) // 4
        
            cv2.circle(
                frame,
                (frame_x, frame_y),
                10,
                (0,0,255),
                -1
            )

        #This part computes dx and dy
        flag = (frame_x is None) or (frame_y is None) or (obj_x is None) or (obj_y is None)
    
        if not flag:
            dx = obj_x - frame_x
            dy = obj_y - frame_y
    
            #This part creates a connection (yellow line) between centers
            cv2.line(
                frame,
                (frame_x, frame_y),
                (obj_x, obj_y),
                (0, 255, 255),
                2
            )
    
            #Direction determination
            THRESHOLD = 15
            
            message = "CENTERED"
            
            # if abs(dx) > THRESHOLD:
            
            #     horizontal = ""
            
            #     if dx > 0:
            #         horizontal = "MOVE LEFT"
            #     else:
            #         horizontal = "MOVE RIGHT"
            
            #     vertical = ""
            
            #     if dy > THRESHOLD:
            #         vertical = "UP"
            
            #     elif dy < -THRESHOLD:
            #         vertical = "DOWN"
            
            #     message = horizontal + " " + vertical
            if abs(dx)>THRESHOLD and abs(dy)>THRESHOLD:
                if dx>0:
                    horizontal = "MOVE LEFT"
                else:
                    horizontal = "MOVE RIGHT"
                if dy>0:
                    vertical = "UP"
                else:
                    vertical = "DOWN"
                message = horizontal+" "+vertical
            elif abs(dx)>THRESHOLD:
                if dx>0:
                    message = "MOVE LEFT"
                else:
                    message = "MOVE RIGHT"
            elif abs(dy)>THRESHOLD:
                if dy>0:
                    message = "MOVE UP"
                else:
                    message = "MOVE DOWN"
    
            cv2.putText(
                frame,
                message,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )
            cv2.putText(
                frame,
                f"dx={dx} dy={dy}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,255),
                2
            )

    cv2.imshow("Aruco", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()