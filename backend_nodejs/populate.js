import mongoose from 'mongoose';
import Baby from './models/baby';

//나중에는 여기에서 json파일 읽어들이는 것으로 고치기!

const babies = [
  { //littleMe2
    0: {
      info: {
        size: { width: 960, height: 801 }
      },
      faceCount: 1
    },
    1: {
      faces: {
        roi: {
          x: 405,
          y: 106,
          width: 94,
          height: 94
        },
        landmart: {
          leftEye: { x: 428, y: 134 },
          rightEye: { x: 471, y: 133 },
          nose: { x: 448, y: 151 },
          leftMouth: { x: 435, y: 181 },
          rightMouth: { x: 462, y: 181 }
        },
        gender: { value: "child", confidence: 0.9895},
        age: { value: "0~2", confidence: 1.0},
        emotion: { value: "neutral", confidence: 0.999995},
        pose: { value: "frontal_face", confidence: 0.999637}
      }
    }
  },
  { //littleMe3
    0: {
      info: {
        size: { width: 960, height: 801 }
      },
      faceCount: 2
    },
    1: {
      faces:
         {
           0: {
            roi: {
              x: 159,
              y: 306,
              width: 167,
              height: 167
            },
            landmart: {
              leftEye: { x: 199, y: 354 },
              rightEye: { x: 274, y: 354 },
              nose: { x: 234, y: 388 },
              leftMouth: { x: 212, y: 431 },
              rightMouth: { x: 269, y: 426 }
            },
            gender: { value: "child", confidence: 0.919942},
            age: { value: "2~6", confidence: 0.755594},
            emotion: { value: "neutral", confidence: 0.695442},
            pose: { value: "frontal_face", confidence: 0.999794}
          },
           1: {
            roi: {
              x: 583,
              y: 272,
              width: 134,
              height: 134
            },
            landmart: null,
            gender: { value: "female", confidence: 0.645616},
            age: { value: "1~5", confidence: 1.0},
            emotion: { value: "talking", confidence: 0.765038},
            pose: { value: "frontal_face", confidence: 0.632905}
          }
         }
      }
    }

];

mongoose.connect('mongodb://localhost/babies');

babies.map(data => {
  const baby = new Baby(data);
  baby.save();
});
