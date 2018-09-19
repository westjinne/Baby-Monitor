import mongoose, { Schema } from 'mongoose';

var babySchema = new Schema({
  info:
    { size:
      { width: Number, height: Number },
       faceCount: Number
    },
  faces:
    { roi :
      { x: Number, y: Number, width: Number, height: Number },
      landmark:
        { leftEye: { x: Number, y: Number },
        rightEye: { x: Number, y: Number },
        nose: { x: Number, y: Number },
        leftMouth: { x: Number, y: Number },
        rightMouth: { x: Number, y: Number }},
      gender: { value: String, confidence: Number },
      age: { value: String, confidence: Number },
      emotion: { value: String, confidence: Number },
      pose: { value: String, confidence: Number }
    },
  });

  export default mongoose.model('baby', babySchema);
