import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.mllib.classification.SVMWithSGD
import org.apache.spark.mllib.evaluation.BinaryClassificationMetrics
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.util.MLUtils
object SVMApp {


 	def main(args: Array[String]) {
 		val conf = new SparkConf().setAppName("Simple Application")
    		val sc = new SparkContext(conf)
		// Load training data in LIBSVM format.
		val s= System.nanoTime
		val data = MLUtils.loadLibSVMFile(sc, "data/mllib/test.txt")

		// Split data into training (60%) and test (40%).
		val splits = data.randomSplit(Array(0.3, 0.7), seed = 11L)
		val training = data.cache()
		val test = splits(1)
		
		println(training)
		// Run training algorithm to build the model
		val numIterations = 100

		val model =time{SVMWithSGD.train(training, numIterations)}
		
		// Clear the default threshold.
		model.clearThreshold()
		val s2 = System.nanoTime
		// Compute raw scores on the test set. 
		val scoreAndLabels = test.map { point =>
		  val score = model.predict(point.features)
		  (score, point.label)
		}

		// Get evaluation metrics.
		val metrics = new BinaryClassificationMetrics(scoreAndLabels)
		println("metrics is:")
		println(metrics)
		val auROC = metrics.areaUnderROC()
		val s3 = System.nanoTime
		val accuracy = 1.0 * scoreAndLabels.filter(x => x._1 * x._2 >=0).count() / test.count()
		println("Accuracy = " + accuracy * 100 + "%")
		println("Area under ROC = " + auROC)
		println("Training time: "+(s2-s)/1e6+"ms\n\n\n\n\n\n\n\n")
		println("Prediction time: "+(s3-s)/1e6+"ms\n\n\n\n\n\n\n\n")
	}

	def time[A](f: => A) = {
		val s= System.nanoTime
		val ret = f
		println("time: "+(System.nanoTime-s)/1e6+"ms")
		ret
	}
}