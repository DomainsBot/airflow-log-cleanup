import unittest

from airflow_log_cleanup.dag import create_dag


class DagSmokeTest(unittest.TestCase):

    def test_it_when_trying_to_instantiate_it_should_succeed(self):
        dag = create_dag()
        self.assertEqual('airflow_log_cleanup', dag.dag_id)
        self.assertIsNotNone(dag.default_args)
