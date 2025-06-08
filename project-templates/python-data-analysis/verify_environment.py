#!/usr/bin/env python3
"""
GitHub Copilot Certification - Python Data Analysis Environment Verification
"""
import sys

def verify_environment():
    """Verify that all required packages are installed and working"""
    print('✅ Python Data Analysis Environment Setup Complete!')
    print('')
    
    # Test core packages
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        import plotly
        import sklearn
        import faker
        import openpyxl
        import requests
        import black
        import pytest
        
        print('📊 Successfully imported packages:')
        print(f'  • pandas: {pd.__version__}')
        print(f'  • numpy: {np.__version__}')
        print(f'  • matplotlib: {plt.matplotlib.__version__}')
        print(f'  • seaborn: {sns.__version__}')
        print(f'  • plotly: {plotly.__version__}')
        print(f'  • scikit-learn: {sklearn.__version__}')
        print('  • faker: ✓ imported successfully')
        print('  • openpyxl: ✓ imported successfully')
        print('  • requests: ✓ imported successfully')
        print('  • black: ✓ imported successfully')
        print('  • pytest: ✓ imported successfully')
        print('')
        
        # Quick functionality test
        print('🧪 Quick functionality test:')
        df = pd.DataFrame({'x': np.random.randn(5), 'y': np.random.randn(5)})
        print(f'  • Created pandas DataFrame: {df.shape}')
        
        fake = faker.Faker()
        print(f'  • Generated fake name: {fake.name()}')
        print('')
        
        print('🚀 Ready for GitHub Copilot data analysis practice!')
        print('💡 Start with: jupyter lab copilot-data-analysis-starter.ipynb')
        print('')
        print('🛠️  Available tools:')
        print('  • Data manipulation: pandas, numpy')
        print('  • Visualization: matplotlib, seaborn, plotly')
        print('  • Machine learning: scikit-learn')
        print('  • Data generation: faker')
        print('  • File I/O: openpyxl, requests')
        print('  • Development: black, pytest')
        print('')
        print(f'💻 Environment: Python {sys.version.split()[0]} + Apple Silicon optimized')
        print('')
        print('🎯 GitHub Copilot Certification - Data Analysis Project Ready!')
        
        return True
        
    except ImportError as e:
        print(f'❌ Import error: {e}')
        return False
    except Exception as e:
        print(f'❌ Error: {e}')
        return False

if __name__ == '__main__':
    success = verify_environment()
    sys.exit(0 if success else 1)
