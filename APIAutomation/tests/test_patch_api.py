import time

from APIAutomation.Utilities.PatchUpdate import PatchUpdate


class TestPatchApi(PatchUpdate):
    def test_patch_api(self):
        payload={
                "userId": 14,
                "id": 1899,
                "title": "vijay",
                "body":f"vijay updated patch {time.strftime('%Y-%m-%d %H:00:00')}"
            }
        patch=PatchUpdate()
        resp=patch.patch_update(json=payload)
        print(resp)
        print(resp.json())
        assert resp.status_code == 200
        assert resp.json()['body']==f"vijay updated patch {time.strftime('%Y-%m-%d %H:00:00')}"

