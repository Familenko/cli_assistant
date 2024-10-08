from collections import defaultdict

class Tags:
    def __init__(self):
        self.tag_to_notes = defaultdict(set)
        self.note_to_tags = defaultdict(set)

    def add_tag(self, note_id, tag):
        self.tag_to_notes[tag].add(note_id)
        self.note_to_tags[note_id].add(tag)

    def remove_tag(self, note_id, tag):
        if note_id in self.tag_to_notes[tag]:
            self.tag_to_notes[tag].remove(note_id)
        if tag in self.note_to_tags[note_id]:
            self.note_to_tags[note_id].remove(tag)

    def get_notes_by_tag(self, tag):
        return list(self.tag_to_notes[tag])

    def get_tags_for_note(self, note_id):
        return list(self.note_to_tags[note_id])

    def search_notes_by_tags(self, tags):
        if not tags:
            return []
        result = set(self.tag_to_notes[tags[0]])
        for tag in tags[1:]:
            result.intersection_update(self.tag_to_notes[tag])
        return list(result)

    def sort_notes_by_tags(self, note_ids):
        return sorted(note_ids, key=lambda note_id: len(self.note_to_tags[note_id]), reverse=True)
