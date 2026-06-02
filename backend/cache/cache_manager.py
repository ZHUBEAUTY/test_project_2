from .redis_cache import RedisCache
from backend.common.config import CACHE_PREFIX

cache = RedisCache()

class CacheManager:
    def get_task(self, task_id):
        return cache.get(f"{CACHE_PREFIX}{task_id}")

    def save_task(self, task):
        cache.set(f"{CACHE_PREFIX}{task.id}", task)

    def invalidate_task(self, task_id):
        cache.delete(task_id)
