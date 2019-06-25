'''
    Quality test :
    This is a benchmark that, for given inputs, execute our recommendation system and other algorithms
    and checks tha our recommendation system's failure score is the lowest
'''

import sys
import unittest

sys.path.append("..")
from surprise import *
from surprise.model_selection import cross_validate

from src.CF_rec import *

import time
import multiprocessing
import concurrent.futures

package_dir = os.path.dirname(os.path.abspath(__file__))
resource_file_path = os.path.join(package_dir,'../Res/clean_reviews.csv')


class TestRecommenderSystem(unittest.TestCase):

    def setUp(self):
        self.bsl_options = {'method': 'als',
                            'n_epochs': 5,
                            'reg_u': 12,
                            'reg_i': 5
                            }
        self.test_ratio = 0.15
        self.rate_scale = (0, 5)
        self.csv = open_csv(resource_file_path)
        self.data = df_to_dataset(self.csv)
        self.benchmark_parallel = []

    def test_open_csv(self):
        # check if columns are correctly retrieved
        self.assertEqual(self.csv.columns[0], 'RecipeID')
        self.assertEqual(self.csv.columns[1], 'profileID')
        self.assertEqual(self.csv.columns[2], 'Rate')
        # check if the data retrieved from csv file is not empty
        self.assertNotEqual(self.csv.shape[0], 0)



    def do_it(self, x):
        if x == 1 :
            print("deb")
            results = cross_validate(SVD(), self.data, measures=['RMSE'], cv=3, verbose=False)
            print("fin svd")
            self.benchmark_parallel.append(results)
        else :
            print("debuut")
            results = cross_validate(BaselineOnly(), self.data, measures=['RMSE'], cv=3, verbose=False)
            self.benchmark_parallel.append(results)
            print("fin bse")


    def test_it(self):
        t = (1, 2)
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as executor :
            result = executor.map(self.do_it, t)
        finish = time.time()
        print(finish - start)


    def test_performance_multi(self):
        print("testing performance of algorithms: SVD, SVDpp, SlopeOne, NMF, NormalPredictor, KNNBaseline,\n"
              "KNNBaseline, KNNBasic, KNNWithMeans, KNNWithZScore , BaselineOnly, CoClustering")
        benchmark = []
        # Iterate over all algorithms

        x = [SVD(), SVDpp(), SlopeOne(), NMF(),
                          NormalPredictor(), KNNBaseline(), KNNBasic(),
                          KNNWithMeans(), KNNWithZScore(), BaselineOnly(), CoClustering()]

        pool = multiprocessing.Pool()
        result = pool.map(self, x)

        for algorithm in [SVD(), SVDpp(), SlopeOne(), NMF(),
                          NormalPredictor(), KNNBaseline(), KNNBasic(),
                          KNNWithMeans(), KNNWithZScore(), BaselineOnly(), CoClustering()]:
            # Perform cross validation
            results = cross_validate(algorithm, self.data, measures=['RMSE'], cv=3, verbose=False)

            # Get results & append algorithm name
            tmp = pd.DataFrame.from_dict(results).mean(axis=0)
            tmp = tmp.append(pd.Series([str(algorithm).split(' ')[0].split('.')[-1]], index=['Algorithm']))
            benchmark.append(tmp)
            bench = pd.DataFrame(benchmark).set_index('Algorithm').sort_values('test_rmse')
        print(bench)
        # check if the BaselineOnly algorithm is the most performant in terms of RMSE
        self.assertEqual(bench.idxmin(axis=0)[0], 'BaselineOnly')

if __name__ == '__main__':
    unittest.main()
