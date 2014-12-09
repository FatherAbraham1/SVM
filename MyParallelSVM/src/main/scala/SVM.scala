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
		val data = MLUtils.loadLibSVMFile(sc, "data/mllib/test.txt")

		// Split data into training (60%) and test (40%).
		val splits = data.randomSplit(Array(0.6, 0.4), seed = 11L)
		val training = splits(0).cache()
		val test = splits(1)
		println("I am here!!!!!!!\n\n\n\n\n")
		println(training)
		// Run training algorithm to build the model
		val numIterations = 100

		val model =time{SVMWithSGD.train(training, numIterations)}
		println("I am here2!!!!!!!\n\n\n\n\n")
		// Clear the default threshold.
		model.clearThreshold()

		// Compute raw scores on the test set. 
		val scoreAndLabels = test.map { point =>
		  val score = model.predict(point.features)
		  (score, point.label)
		}
		println("I am here3!!!!!!!\n\n\n\n\n")
		// Get evaluation metrics.
		val metrics = new BinaryClassificationMetrics(scoreAndLabels)
		val auROC = metrics.areaUnderROC()

		println("Area under ROC = " + auROC)
	}

	def time[A](f: => A) = {
		val s= System.nanoTime
		val ret = f
		println("time: "+(System.nanoTime-s)/1e6+"ms")
		ret
	}
}