# Magic Square Solver Using Hyper-Heuristics and Hill Climbing

This repository contains Python code for solving the magic square problem using two optimisation techniques: **Selection Hyper-Heuristics** and **Hill Climbing**. The code implements both approaches and allows users to experiment with the solution methods.

The main focus is on **Selection Hyper-Heuristics** based on the tutorial from:
> **Ahmed Kheiri and Ed Keedwell (2022)**, *Selection Hyper-Heuristics*. In Proceedings of the Genetic and Evolutionary Computation Conference Companion, GECCO '22, pages 983-996, New York, NY, USA. ACM.  
> [http://dx.doi.org/10.1145/3520304.3533655](http://dx.doi.org/10.1145/3520304.3533655)

If you're interested in exploring a more challenging constrained version of the magic square problem, refer to the following paper:
> **Ahmed Kheiri and Ender Ozcan (2014)**, *Constructing Constrained-Version of Magic Squares Using Selection Hyper-Heuristics*. The Computer Journal, 57(3):469-479.  
> [Link to the paper](https://ahmedkheiri.github.io/publications/TheComputerJournal2014.pdf) | [DOI](http://dx.doi.org/10.1093/comjnl/bxt130)

## Features

- **Magic Square Solver**: Implements the magic square problem solver using two methods:
  1. **Simple Random Hyper-Heuristic (SRHH)**: Optimises the solution by applying a sequence of low-level heuristics (LLHs).
  2. **Hill Climbing**: A local search algorithm that improves the solution by performing random swaps of elements.

- **Configurable**: You can easily change the size of the magic square (default is 3x3).

- **Extensible**: The framework supports additional low-level heuristics and optimisation techniques.

## Requirements

- Python 3.x
- Standard Python libraries: `random`, `copy`

## Usage

To run the magic square solver, clone this repository and execute the main Python file. The code allows you to select between the two methods: **SRHH** or **Hill Climbing**.

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmedkheiri/magic-square.git
   cd magic-square
2. Run the Python script:
   ```bash
   python magic_square.py

By default, the code runs the **Selection Hyper-Heuristic** (`SRHH`). To switch to **Hill Climbing**, comment/uncomment the appropriate line in the `__main__` section of the code.

### Example

	```python
	# Apply Simple Random Hyper-Heuristic (SRHH) algorithm
	sol = SRHH(sol)

	# Uncomment to apply Hill Climbing algorithm
	# sol = HillClimbing(sol)

## Citing This Work

If you use this code or adapt it for your research or projects, please cite the following paper:

> **Ahmed Kheiri and Ed Keedwell (2022)**, *Selection Hyper-Heuristics*. In Proceedings of the Genetic and Evolutionary Computation Conference Companion, GECCO '22, pages 983-996, New York, NY, USA. ACM.  
> [http://dx.doi.org/10.1145/3520304.3533655](http://dx.doi.org/10.1145/3520304.3533655)

If you're interested in exploring the more challenging constrained version of the magic square problem, please refer to this work:

> **Ahmed Kheiri and Ender Ozcan (2014)**, *Constructing Constrained-Version of Magic Squares Using Selection Hyper-Heuristics*. The Computer Journal, 57(3):469-479.  
> [Link to the paper](https://ahmedkheiri.github.io/publications/TheComputerJournal2014.pdf) | [DOI](http://dx.doi.org/10.1093/comjnl/bxt130)

### Future Work

- Extend the number of low-level heuristics (LLHs) for the hyper-heuristic search.
- Implement additional optimisation algorithms, such as Simulated Annealing or Tabu Search.
- Introduce more constraints based on the second paper to create harder instances of the magic square problem.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
