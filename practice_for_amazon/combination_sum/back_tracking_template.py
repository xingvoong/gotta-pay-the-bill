def backtrack(candidate):
  if find_solution(candidate):
    output(candidate)
    return

  # iterate all possible candidates
  for next_candidate in list_of_candidates:
    if is_valid(next_candidate):
      # try this partial candidate solution
      place(next_candidate)
      # given the candidate, explore futher
      backtrack(next_candidate)
      remove(next_candidate)