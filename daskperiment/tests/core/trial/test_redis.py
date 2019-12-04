from daskperiment.backend.redis import RedisBackend
from daskperiment.testing import CleanupMixin
from daskperiment.tests.core.trial.base import TrialManagerBase


class TestRedisTrialManager(TrialManagerBase, CleanupMixin):

    backend = 'redis://localhost:6379/0'

    @property
    def trials(self):
        backend = RedisBackend('dummy', self.backend)
        return backend.get_trial_manager()

    def test_init(self):
        # test trial_id is properly initialized
        backend = RedisBackend('init', self.backend)
        t = backend.get_trial_manager()
        assert t.trial_id == 0
        assert not t.is_locked()
