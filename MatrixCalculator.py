import numpy as np

def get_matrix():
    """Get matrix input from user with proper validation."""
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        
        if rows <= 0 or cols <= 0:
            raise ValueError("Dimensions must be positive integers.")
            
        print("Enter the matrix row by row, with elements separated by spaces:")
        elements = []
        for i in range(rows):
            while True:
                try:
                    row_input = input(f"Row {i+1}: ").strip()
                    if not row_input:
                        raise ValueError("Empty row input.")
                    row = list(map(float, row_input.split()))
                    if len(row) != cols:
                        raise ValueError(f"Expected {cols} elements, got {len(row)}.")
                    elements.append(row)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")
                    
        return np.array(elements)
    except ValueError as e:
        print("ERROR:", e)
        return None
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return None

def get_vector():
    """Get vector input from user."""
    try:
        size = int(input("Enter the vector size: "))
        if size <= 0:
            raise ValueError("Vector size must be positive.")
            
        print("Enter vector elements separated by spaces:")
        while True:
            try:
                elements_input = input().strip()
                if not elements_input:
                    raise ValueError("Empty vector input.")
                elements = list(map(float, elements_input.split()))
                if len(elements) != size:
                    raise ValueError(f"Expected {size} elements, got {len(elements)}.")
                return np.array(elements)
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
                
    except ValueError as e:
        print("ERROR:", e)
        return None
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return None

def get_scalar():
    """Get scalar input from user."""
    try:
        return float(input("Enter scalar value: "))
    except ValueError:
        print("ERROR: Invalid scalar value.")
        return None
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return None

def safe_operation(operation, *args, operation_name="Operation"):
    """Safely execute an operation with error handling."""
    try:
        result = operation(*args)
        return result, None
    except np.linalg.LinAlgError as e:
        return None, f"{operation_name}: Linear algebra error - {str(e)}"
    except ValueError as e:
        return None, f"{operation_name}: Value error - {str(e)}"
    except Exception as e:
        return None, f"{operation_name}: Unexpected error - {str(e)}"

def matrix_operations(A, B):
    """Perform various matrix operations."""
    print(f"\nMatrix A ({A.shape}):\n{A}")
    print(f"\nMatrix B ({B.shape}):\n{B}")
    
    operations = [
        (lambda: A + B, "Addition"),
        (lambda: A - B, "Subtraction"), 
        (lambda: np.dot(A, B), "Matrix Multiplication"),
        (lambda: A * B, "Element-wise Multiplication"),
        (lambda: A.T, "Transpose of A"),
        (lambda: B.T, "Transpose of B"),
        (lambda: np.linalg.det(A), "Determinant of A"),
        (lambda: np.linalg.det(B), "Determinant of B"),
        (lambda: np.linalg.inv(A), "Inverse of A"),
        (lambda: np.linalg.inv(B), "Inverse of B"),
    ]
    
    for operation, name in operations:
        result, error = safe_operation(operation, operation_name=name)
        if error:
            print(f"\n{error}")
        else:
            print(f"\n{name}:\n{result}")

def vector_operations(v1, v2=None, scalar=None):
    """Perform vector operations."""
    print(f"\nVector 1 ({v1.shape}): {v1}")
    
    if v2 is not None:
        print(f"Vector 2 ({v2.shape}): {v2}")
        
        operations = [
            (lambda: v1 + v2, "Vector Addition"),
            (lambda: v1 - v2, "Vector Subtraction"),
            (lambda: np.dot(v1, v2), "Dot Product"),
            (lambda: np.linalg.norm(v1 - v2), "Euclidean Distance"),
        ]
        
        # Cross product only for 3D vectors
        if len(v1) == 3 and len(v2) == 3:
            operations.append((lambda: np.cross(v1, v2), "Cross Product"))
            
    else:
        operations = []
    
    # Vector properties
    norm_result, norm_error = safe_operation(lambda: np.linalg.norm(v1), operation_name="Norm of Vector 1")
    if norm_error:
        print(f"\n{norm_error}")
    else:
        print(f"\nNorm of Vector 1: {norm_result}")
        
    # Unit vector
    unit_result, unit_error = safe_operation(lambda: v1 / np.linalg.norm(v1), operation_name="Unit Vector 1")
    if unit_error:
        print(f"\n{unit_error}")
    else:
        print(f"Unit Vector 1: {unit_result}")
    
    # Vector operations with second vector
    for operation, name in operations:
        result, error = safe_operation(operation, operation_name=name)
        if error:
            print(f"\n{error}")
        else:
            print(f"\n{name}: {result}")
    
    # Scalar operations if scalar provided
    if scalar is not None:
        print(f"\nScalar: {scalar}")
        print(f"Scalar Multiplication: {v1 * scalar}")
        if scalar != 0:
            print(f"Scalar Division: {v1 / scalar}")
        else:
            print("Scalar Division: ERROR - Division by zero")

def scalar_matrix_operations(matrix, scalar):
    """Perform scalar-matrix operations."""
    print(f"\nMatrix ({matrix.shape}):\n{matrix}")
    print(f"Scalar: {scalar}")
    
    print(f"\nScalar Addition:\n{matrix + scalar}")
    print(f"\nScalar Multiplication:\n{matrix * scalar}")
    print(f"\nScalar Power:\n{np.power(matrix, scalar)}")
    
    if scalar != 0:
        print(f"\nScalar Division:\n{matrix / scalar}")
    else:
        print("\nScalar Division: ERROR - Division by zero")

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("ENHANCED MATRIX/VECTOR/SCALAR CALCULATOR")
    print("="*50)
    print("1. Matrix Operations (A op B)")
    print("2. Vector Operations") 
    print("3. Scalar-Matrix Operations")
    print("4. Matrix Properties")
    print("5. Vector Properties")
    print("0. Exit")
    print("="*50)

def matrix_properties(matrix):
    """Display various matrix properties."""
    print(f"\nMatrix ({matrix.shape}):\n{matrix}")
    
    properties = [
        (lambda: matrix.T, "Transpose"),
        (lambda: np.trace(matrix), "Trace"),
        (lambda: np.linalg.det(matrix), "Determinant"),
        (lambda: np.linalg.matrix_rank(matrix), "Rank"),
        (lambda: np.linalg.cond(matrix), "Condition Number"),
        (lambda: np.linalg.inv(matrix), "Inverse"),
        (lambda: np.linalg.eigvals(matrix), "Eigenvalues"),
    ]
    
    for operation, name in properties:
        result, error = safe_operation(operation, operation_name=name)
        if error:
            print(f"\n{error}")
        else:
            print(f"\n{name}:\n{result}")

def main():
    """Main program loop."""
    while True:
        display_menu()
        try:
            choice = input("Enter your choice (0-5): ").strip()
            
            if choice == '0':
                print("Thank you for using the calculator!")
                break
                
            elif choice == '1':
                print("\n--- MATRIX OPERATIONS ---")
                print("Input Matrix A:")
                A = get_matrix()
                if A is None:
                    continue
                    
                print("\nInput Matrix B:")
                B = get_matrix()
                if B is None:
                    continue
                    
                matrix_operations(A, B)
                
            elif choice == '2':
                print("\n--- VECTOR OPERATIONS ---")
                print("Input Vector 1:")
                v1 = get_vector()
                if v1 is None:
                    continue
                
                two_vectors = input("Do you want to work with two vectors? (y/n): ").lower().startswith('y')
                v2 = None
                if two_vectors:
                    print("Input Vector 2:")
                    v2 = get_vector()
                    if v2 is None:
                        continue
                
                scalar_op = input("Do you want to include scalar operations? (y/n): ").lower().startswith('y')
                scalar = None
                if scalar_op:
                    scalar = get_scalar()
                    if scalar is None:
                        continue
                        
                vector_operations(v1, v2, scalar)
                
            elif choice == '3':
                print("\n--- SCALAR-MATRIX OPERATIONS ---")
                print("Input Matrix:")
                matrix = get_matrix()
                if matrix is None:
                    continue
                    
                scalar = get_scalar()
                if scalar is None:
                    continue
                    
                scalar_matrix_operations(matrix, scalar)
                
            elif choice == '4':
                print("\n--- MATRIX PROPERTIES ---")
                print("Input Matrix:")
                matrix = get_matrix()
                if matrix is None:
                    continue
                    
                matrix_properties(matrix)
                
            elif choice == '5':
                print("\n--- VECTOR PROPERTIES ---")
                print("Input Vector:")
                vector = get_vector()
                if vector is None:
                    continue
                    
                vector_operations(vector)
                
            else:
                print("Invalid choice. Please enter a number between 0-5.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()