import io
import pytest
from collect_info_and_order import collect_info

# Test for collect info function
# class TestCollectInfo:
#     def test_collect_name(self, monkeypatch):
#         monkeypatch.setattr('sys.stdin', io.StringIO('56'))
#         try:
#             collect_info()
#         except ValueError:
#             assert False

#     def test_value_error(self):
#         with pytest.raises(ValueError):
#             name = 'Alex'
#             name == float(name)