import torch


def check_torch():
    try:
        # Check PyTorch version
        print(f"PyTorch version: {torch.__version__}")

        # Perform a simple tensor operation
        x = torch.rand(5, 3)
        print(f"Successfully created a random tensor:\n{x}")

        # Check if CUDA is available
        if torch.cuda.is_available():
            print("CUDA is available! Here are the details:")
            print(f"CUDA version: {torch.version.cuda}")
            print(f"Number of CUDA devices: {torch.cuda.device_count()}")
            for i in range(torch.cuda.device_count()):
                print(f"Device {i}: {torch.cuda.get_device_name(i)}")

            # Perform a simple tensor operation on GPU
            device = torch.device("cuda")
            y = torch.rand(5, 3, device=device)
            print(f"Successfully created a random tensor on GPU:\n{y}")
        else:
            print("CUDA is not available. Please check your installation.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure PyTorch is properly installed.")


if __name__ == "__main__":
    check_torch()
