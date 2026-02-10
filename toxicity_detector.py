def detect_toxicity (data_buffer, thresold=10):
  if length (data_buffer) < 7:
    return False
  recent = data_buffer[-7:]
  rising = all(a < b for a, b in zip(recent, recent[1:]))
  near_thresold = thresold
  return rising and near_thresold
