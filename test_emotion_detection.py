# Import the 'unittest' module
import unittest

from EmotionDetection import emotion_detection

#Class for emotion_detector testing
class TestEmotionDetetor(unittest.TestCase): 
    
        def test_DominantEmotion(self): 

            result1=emotion_detection.emotion_detector("I am glad this happen")
            self.assertEqual(result1["dominant emotion"],"joy")

            result2=emotion_detection.emotion_detector("I am really mad about this")
            self.assertEqual(result2["dominant emotion"],"anger")

            result3=emotion_detection.emotion_detector("I feel disgusted just hearing about this")
            self.assertEqual(result3["dominant emotion"],"disgust")

            result4=emotion_detection.emotion_detector("I am so sad about this")
            self.assertEqual(result4["dominant emotion"],"sadness")

            result5=emotion_detection.emotion_detector("I am really afraid that this will happen")
            self.assertEqual(result5["dominant emotion"],"fear")

if __name__ == '__main__':
    unittest.main()