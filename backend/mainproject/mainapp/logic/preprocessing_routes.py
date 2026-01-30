# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
# from sklearn.impute import SimpleImputer, KNNImputer
# import warnings
# warnings.filterwarnings('ignore')

# def run_preprocessing_pipeline(file, operations=None, original_filename=None, column_operations=None):
#     """
#     Smart preprocessing pipeline that handles any dataset with maximum accuracy
#     """
#     logs = []
#     download_info = None
    
#     try:
#         # Step 1: Smart CSV reading with error handling
#         df, read_logs = smart_read_csv(file)
#         logs.extend(read_logs)

#         if df.empty:
#             return df, logs, None

#         original_shape = df.shape
#         logs.append(f"✅ Dataset loaded: {original_shape[0]} rows × {original_shape[1]} columns")

#         # Step 2: Comprehensive data profiling
#         profile_logs = data_profiling(df)
#         logs.extend(profile_logs)

#         # Step 3: Use column operations if provided, otherwise get AI suggestions
#         if column_operations:
#             logs.append(f"🎯 Executing column-wise operations: {column_operations}")
#             df = execute_column_wise_operations(df, column_operations, logs)
#         elif operations:
#             logs.append(f"🎯 Executing operations: {operations}")
#             df = execute_smart_operations(df, operations, logs)
#         else:
#             operations = get_ai_suggestions(df, logs)
#             logs.append(f"🎯 Executing AI operations: {operations}")
#             df = execute_smart_operations(df, operations, logs)
        
#         # Step 4: Final data quality check
#         quality_logs = final_quality_check(df, original_shape)
#         logs.extend(quality_logs)

#         # Step 5: Save processed file
#         if original_filename:
#             download_info = save_processed_file(df, original_filename)
#             logs.append(f"💾 Processed file saved: {download_info['filename']}")

#         logs.append("🎉 Preprocessing completed successfully!")

#         return df, logs, download_info

#     except Exception as e:
#         error_msg = f"❌ Preprocessing failed: {str(e)}"
#         logs.append(error_msg)
#         return pd.DataFrame(), logs, None

# def execute_column_wise_operations(df, column_operations, logs):
#     """Execute column-wise operations with maximum accuracy"""
#     executed_ops = []
    
#     # Handle dataset-wide operations first
#     if "dataset_wide" in column_operations:
#         for operation in column_operations["dataset_wide"]:
#             df = execute_single_operation(df, operation, "dataset_wide", logs)
#             executed_ops.append(f"dataset_wide:{operation}")
    
#     # Handle column-specific operations
#     for column, operations in column_operations.items():
#         if column == "dataset_wide":
#             continue
            
#         if column not in df.columns:
#             logs.append(f"⚠️  Column '{column}' not found in dataset. Skipping operations.")
#             continue
            
#         for operation in operations:
#             df = execute_single_operation(df, operation, column, logs)
#             executed_ops.append(f"{column}:{operation}")
    
#     if executed_ops:
#         logs.append(f"✅ Executed column operations: {executed_ops}")
    
#     return df

# def execute_single_operation(df, operation, column, logs):
#     """Execute a single operation on a specific column with maximum accuracy"""
#     try:
#         if column == "dataset_wide":
#             # Dataset-wide operations
#             if operation == "remove:duplicates":
#                 initial_count = len(df)
#                 df = df.drop_duplicates()
#                 removed = initial_count - len(df)
#                 if removed > 0:
#                     logs.append(f"🧹 Removed {removed} duplicate rows")
            
#             elif operation == "validate:datatypes":
#                 conversions = smart_validate_datatypes_single(df, logs)
#                 if conversions:
#                     logs.append(f"🔍 Data type validation: {', '.join(conversions)}")
        
#         else:
#             # Column-specific operations
#             if operation == "impute:mean":
#                 if pd.api.types.is_numeric_dtype(df[column]):
#                     # Only impute if there are missing values
#                     missing_count = df[column].isnull().sum()
#                     if missing_count > 0:
#                         # Check for invalid zeros that should be treated as missing
#                         zero_count = (df[column] == 0).sum()
#                         total_valid = len(df[column]) - missing_count
                        
#                         # For Age-like columns, treat 0 as missing if it's suspicious
#                         if column.lower() in ['age', 'experience', 'salary'] and zero_count > 0:
#                             if zero_count < total_valid * 0.5:  # If less than 50% zeros
#                                 # Treat zeros as missing for numeric columns
#                                 temp_series = df[column].replace(0, np.nan)
#                                 mean_val = temp_series.mean()
#                                 df[column] = df[column].replace(0, np.nan).fillna(mean_val)
#                                 logs.append(f"📊 {column}: imputed {missing_count + zero_count} values (missing+zeros) with mean ({mean_val:.2f})")
#                             else:
#                                 mean_val = df[column].mean()
#                                 df[column] = df[column].fillna(mean_val)
#                                 logs.append(f"📊 {column}: imputed {missing_count} missing values with mean ({mean_val:.2f})")
#                         else:
#                             mean_val = df[column].mean()
#                             df[column] = df[column].fillna(mean_val)
#                             logs.append(f"📊 {column}: imputed {missing_count} missing values with mean ({mean_val:.2f})")
            
#             elif operation == "impute:median":
#                 if pd.api.types.is_numeric_dtype(df[column]):
#                     missing_count = df[column].isnull().sum()
#                     if missing_count > 0:
#                         # Check for invalid zeros
#                         zero_count = (df[column] == 0).sum()
#                         total_valid = len(df[column]) - missing_count
                        
#                         # For Age-like columns, treat 0 as missing if it's suspicious
#                         if column.lower() in ['age', 'experience', 'salary'] and zero_count > 0:
#                             if zero_count < total_valid * 0.5:
#                                 temp_series = df[column].replace(0, np.nan)
#                                 median_val = temp_series.median()
#                                 df[column] = df[column].replace(0, np.nan).fillna(median_val)
#                                 logs.append(f"📊 {column}: imputed {missing_count + zero_count} values (missing+zeros) with median ({median_val:.2f})")
#                             else:
#                                 median_val = df[column].median()
#                                 df[column] = df[column].fillna(median_val)
#                                 logs.append(f"📊 {column}: imputed {missing_count} missing values with median ({median_val:.2f})")
#                         else:
#                             median_val = df[column].median()
#                             df[column] = df[column].fillna(median_val)
#                             logs.append(f"📊 {column}: imputed {missing_count} missing values with median ({median_val:.2f})")
            
#             elif operation == "impute:mode":
#                 if pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_categorical_dtype(df[column]):
#                     missing_count = df[column].isnull().sum()
#                     if missing_count > 0:
#                         # Clean data first
#                         df[column] = clean_categorical_data(df[column])
                        
#                         if not df[column].mode().empty:
#                             mode_val = df[column].mode()[0]
#                             df[column] = df[column].fillna(mode_val)
#                             logs.append(f"🏷️  {column}: imputed {missing_count} missing values with mode ('{mode_val}')")
#                         else:
#                             df[column] = df[column].fillna('Unknown')
#                             logs.append(f"🏷️  {column}: imputed {missing_count} missing values with 'Unknown'")
            
#             elif operation == "scale:standard":
#                 if pd.api.types.is_numeric_dtype(df[column]):
#                     # Only scale if there's variation and no missing values
#                     if df[column].nunique() > 1 and df[column].isnull().sum() == 0:
#                         # Don't scale if all values are the same
#                         if df[column].std() > 0:
#                             scaler = StandardScaler()
#                             df[column] = scaler.fit_transform(df[[column]]).flatten()
#                             logs.append(f"⚖️  {column}: standardized scaling applied")
#                         else:
#                             logs.append(f"⚠️  {column}: skipping standardization (no variation)")
#                     else:
#                         logs.append(f"⚠️  {column}: skipping standardization (no variation or missing values)")
            
#             elif operation == "scale:minmax":
#                 if pd.api.types.is_numeric_dtype(df[column]):
#                     if df[column].nunique() > 1 and df[column].isnull().sum() == 0:
#                         if df[column].std() > 0:
#                             scaler = MinMaxScaler()
#                             df[column] = scaler.fit_transform(df[[column]]).flatten()
#                             logs.append(f"⚖️  {column}: min-max scaling applied (0-1 range)")
#                         else:
#                             logs.append(f"⚠️  {column}: skipping min-max scaling (no variation)")
#                     else:
#                         logs.append(f"⚠️  {column}: skipping min-max scaling (no variation or missing values)")
            
#             elif operation == "handle:outliers":
#                 if pd.api.types.is_numeric_dtype(df[column]):
#                     if df[column].nunique() > 2 and df[column].std() > 0:  # Need variation for outlier detection
#                         Q1 = df[column].quantile(0.25)
#                         Q3 = df[column].quantile(0.75)
#                         IQR = Q3 - Q1
                        
#                         if IQR > 0:
#                             lower_bound = Q1 - 1.5 * IQR
#                             upper_bound = Q3 + 1.5 * IQR
                            
#                             # Identify outliers
#                             outlier_mask = (df[column] < lower_bound) | (df[column] > upper_bound)
#                             outliers = outlier_mask.sum()
                            
#                             if outliers > 0:
#                                 # Cap outliers instead of removing
#                                 df.loc[outlier_mask, column] = np.where(
#                                     df.loc[outlier_mask, column] < lower_bound, 
#                                     lower_bound, 
#                                     upper_bound
#                                 )
#                                 logs.append(f"📏 {column}: capped {outliers} outliers (bounds: {lower_bound:.2f}-{upper_bound:.2f})")
            
#             elif operation == "encode:onehot":
#                 if pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_categorical_dtype(df[column]):
#                     # Clean categorical data first
#                     df[column] = clean_categorical_data(df[column])
                    
#                     unique_count = df[column].nunique()
#                     if unique_count <= 15 and unique_count > 1:  # Reasonable limit for one-hot
#                         # Use proper one-hot encoding
#                         encoded = pd.get_dummies(df[column], prefix=column, drop_first=True)
#                         df = pd.concat([df, encoded], axis=1)
#                         df.drop(column, axis=1, inplace=True)
#                         logs.append(f"🔤 {column}: one-hot encoded into {len(encoded.columns)} columns")
#                     else:
#                         logs.append(f"⚠️  {column}: unsuitable for one-hot encoding ({unique_count} categories)")
            
#             elif operation == "encode:label":
#                 if pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_categorical_dtype(df[column]):
#                     # Clean categorical data first
#                     df[column] = clean_categorical_data(df[column])
                    
#                     # Handle missing values before encoding
#                     if df[column].isnull().sum() > 0:
#                         df[column] = df[column].fillna('Unknown')
                    
#                     le = LabelEncoder()
#                     df[column] = le.fit_transform(df[column].astype(str))
#                     logs.append(f"🔤 {column}: label encoded ({len(le.classes_)} categories)")
            
#             elif operation == "clean:text":
#                 if pd.api.types.is_object_dtype(df[column]):
#                     original_sample = df[column].iloc[0] if len(df[column]) > 0 else ""
#                     df[column] = clean_categorical_data(df[column])
#                     new_sample = df[column].iloc[0] if len(df[column]) > 0 else ""
                    
#                     if original_sample != new_sample:
#                         logs.append(f"🧹 {column}: text cleaning applied")
            
#             elif operation == "drop:column":
#                 if column in df.columns:
#                     df.drop(column, axis=1, inplace=True)
#                     logs.append(f"🗑️  {column}: column dropped")
        
#         return df
        
#     except Exception as e:
#         logs.append(f"⚠️  Operation '{operation}' on '{column}' failed: {str(e)}")
#         return df

# def clean_categorical_data(series):
#     """Clean and standardize categorical data with maximum accuracy"""
#     # Handle missing values first
#     series = series.fillna('Unknown')
    
#     # Convert to string
#     series = series.astype(str)
    
#     # Replace various null representations
#     null_patterns = ['nan', 'None', 'NULL', 'null', 'NaN', 'none', '']
#     series = series.replace(null_patterns, 'Unknown')
    
#     # Standardize text: trim, lowercase, remove extra spaces
#     series = series.str.strip().str.lower()
#     series = series.str.replace(r'\s+', ' ', regex=True)
    
#     # Special handling for gender-like columns
#     if series.name and ('gender' in series.name.lower() or 'sex' in series.name.lower()):
#         series = series.replace({
#             'm': 'male', 'male': 'male', 'male.': 'male',
#             'f': 'female', 'female': 'female', 'female.': 'female',
#             'unknown': 'unknown'
#         })
    
#     # Special handling for name columns (don't modify names too much)
#     if series.name and 'name' in series.name.lower():
#         # Just capitalize first letter of each word
#         series = series.str.title()
#     else:
#         # For other categorical data, capitalize first letter
#         series = series.str.title()
    
#     return series

# def smart_validate_datatypes_single(df, logs):
#     """Validate and convert data types intelligently"""
#     conversions = []
    
#     for col in df.columns:
#         current_dtype = df[col].dtype
        
#         if df[col].dtype == 'object':
#             # Try to convert to numeric - be more strict
#             numeric_vals = pd.to_numeric(df[col], errors='coerce')
#             numeric_count = numeric_vals.notna().sum()
            
#             # For columns that should be numeric but have some text, be careful
#             if col.lower() in ['age', 'salary', 'experience', 'performance_score']:
#                 if numeric_count > len(df) * 0.8:  # 80% convertible for known numeric columns
#                     df[col] = numeric_vals
#                     conversions.append(f"{col}: object→numeric")
#             else:
#                 if numeric_count > len(df) * 0.95:  # 95% convertible for other columns
#                     df[col] = numeric_vals
#                     conversions.append(f"{col}: object→numeric")
            
#             # Convert to categorical if low cardinality but not too low
#             if df[col].nunique() <= 30 and df[col].nunique() > 1:
#                 df[col] = df[col].astype('category')
#                 conversions.append(f"{col}: object→category")
    
#     return conversions

# def smart_read_csv(file):
#     """Intelligent CSV reading with maximum accuracy"""
#     logs = []
#     try:
#         if isinstance(file, str):
#             df = pd.read_csv(file)
#         else:
#             df = pd.read_csv(file)
        
#         # Auto-detect and fix common CSV issues
#         df = fix_common_csv_issues(df, logs)
        
#         logs.append("✅ CSV read successfully with auto-correction")
#         return df, logs
        
#     except Exception as e:
#         logs.append(f"❌ Failed to read CSV: {str(e)}")
#         return pd.DataFrame(), logs

# def fix_common_csv_issues(df, logs):
#     """Fix common CSV parsing issues with maximum accuracy"""
#     fixes = []
    
#     # Remove extra spaces from column names
#     original_cols = df.columns.tolist()
#     df.columns = df.columns.str.strip()
#     if original_cols != df.columns.tolist():
#         fixes.append("trimmed column spaces")
    
#     # Convert common null representations to actual NaN
#     null_patterns = ['Null', 'null', 'NA', 'N/A', 'NaN', 'nan', 'None', 'none', '']
#     null_count = df.isin(null_patterns).sum().sum()
#     if null_count > 0:
#         df.replace(null_patterns, np.nan, inplace=True)
#         fixes.append(f"converted {null_count} text nulls to NaN")
    
#     # Auto-detect numeric columns stored as objects - be more accurate
#     numeric_conversions = []
#     for col in df.select_dtypes(include=['object']).columns:
#         # Try to convert to numeric
#         numeric_vals = pd.to_numeric(df[col], errors='coerce')
#         non_null_count = numeric_vals.notna().sum()
        
#         # For known numeric columns, be more aggressive
#         if col.lower() in ['age', 'salary', 'experience', 'performance_score']:
#             if non_null_count > len(df) * 0.7:  # 70% convertible for known numeric columns
#                 df[col] = numeric_vals
#                 numeric_conversions.append(col)
#         else:
#             # Only convert if >95% convertible and has reasonable numeric range
#             if (non_null_count > len(df) * 0.95 and 
#                 numeric_vals.nunique() > 1 and 
#                 (numeric_vals.max() - numeric_vals.min()) > 0):
#                 df[col] = numeric_vals
#                 numeric_conversions.append(col)
    
#     if numeric_conversions:
#         fixes.append(f"auto-converted to numeric: {numeric_conversions}")
    
#     if fixes:
#         logs.append(f"🔧 Auto-fixes applied: {', '.join(fixes)}")
    
#     return df

# def data_profiling(df):
#     """Comprehensive data profiling with maximum accuracy"""
#     logs = []
    
#     # Basic stats
#     logs.append(f"📊 Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
#     # Missing values analysis
#     missing_stats = df.isnull().sum()
#     total_missing = missing_stats.sum()
#     missing_percent = (total_missing / (df.shape[0] * df.shape[1])) * 100
    
#     logs.append(f"🔍 Missing Values: {total_missing} total ({missing_percent:.1f}%)")
    
#     if total_missing > 0:
#         high_missing = missing_stats[missing_stats > 0].sort_values(ascending=False)
#         missing_info = [f"{col}({count})" for col, count in high_missing.items()]
#         logs.append(f"   Columns with missing values: {', '.join(missing_info)}")
    
#     # Data types overview
#     dtype_counts = df.dtypes.value_counts()
#     dtype_info = [f"{dtype}({count})" for dtype, count in dtype_counts.items()]
#     logs.append(f"📈 Data Types: {', '.join(dtype_info)}")
    
#     # Duplicate analysis
#     duplicate_count = df.duplicated().sum()
#     if duplicate_count > 0:
#         logs.append(f"⚠️  Duplicate Rows: {duplicate_count}")
    
#     # Column-specific insights
#     for col in df.columns:
#         col_logs = analyze_column(df[col], col)
#         logs.extend(col_logs)
    
#     return logs

# def analyze_column(series, col_name):
#     """Deep analysis of each column with maximum accuracy"""
#     logs = []
#     dtype = series.dtype
#     missing = series.isnull().sum()
#     unique_count = series.nunique()
    
#     logs.append(f"   📍 {col_name}: {dtype}, {missing} missing, {unique_count} unique")
    
#     if pd.api.types.is_numeric_dtype(series):
#         if len(series) > 0:
#             # Check for suspicious zeros
#             zero_count = (series == 0).sum()
#             total_non_missing = len(series) - missing
            
#             if zero_count > 0:
#                 zero_percent = (zero_count / total_non_missing) * 100
#                 if zero_percent < 50:  # If less than 50% zeros, they might be invalid
#                     logs.append(f"      ⚠️  Contains {zero_count} suspicious zero values ({zero_percent:.1f}%)")
#                 else:
#                     logs.append(f"      📊 Contains {zero_count} zero values ({zero_percent:.1f}%)")
            
#             if missing == 0 and total_non_missing > 0:
#                 stats = f"min={series.min():.2f}, max={series.max():.2f}, mean={series.mean():.2f}, std={series.std():.2f}"
#                 logs.append(f"      📊 {stats}")
                
#                 # Check for potential outliers
#                 if series.std() > 0:
#                     Q1 = series.quantile(0.25)
#                     Q3 = series.quantile(0.75)
#                     IQR = Q3 - Q1
#                     if IQR > 0:
#                         lower_bound = Q1 - 1.5 * IQR
#                         upper_bound = Q3 + 1.5 * IQR
#                         outliers = ((series < lower_bound) | (series > upper_bound)).sum()
#                         if outliers > 0:
#                             logs.append(f"      📏 Potential outliers: {outliers}")
    
#     elif pd.api.types.is_string_dtype(series) or pd.api.types.is_object_dtype(series):
#         if unique_count <= 20:
#             top_values = series.value_counts().head(3)
#             top_info = [f"{val}({count})" for val, count in top_values.items()]
#             logs.append(f"      🏷️  Top values: {', '.join(top_info)}")
#         else:
#             logs.append(f"      🔤 High cardinality: {unique_count} categories")
    
#     return logs

# def execute_smart_operations(df, operations, logs):
#     """Execute operations with maximum accuracy"""
#     operation_handlers = {
#         "remove:duplicates": smart_remove_duplicates,
#         "validate:datatypes": smart_validate_datatypes,
#         "impute:auto": smart_impute_auto,
#         "encode:categorical": smart_encode_categorical,
#         "handle:outliers": smart_handle_outliers,
#         "scale:auto": smart_scale_features,
#     }
    
#     for operation in operations:
#         try:
#             if operation in operation_handlers:
#                 df = operation_handlers[operation](df, logs)
#             else:
#                 # Fallback to basic operation
#                 df = execute_basic_operation(df, operation, logs)
#         except Exception as e:
#             logs.append(f"⚠️  Operation '{operation}' skipped: {str(e)}")
#             continue
    
#     return df

# def smart_remove_duplicates(df, logs):
#     """Smart duplicate removal with analysis"""
#     initial_count = len(df)
#     df = df.drop_duplicates()
#     removed = initial_count - len(df)
#     if removed > 0:
#         logs.append(f"🧹 Removed {removed} duplicate rows ({removed/initial_count*100:.1f}%)")
#     return df

# def smart_impute_auto(df, logs):
#     """Intelligent imputation based on data characteristics"""
#     imputations = []
    
#     for col in df.columns:
#         missing_count = df[col].isnull().sum()
        
#         if missing_count == 0:
#             continue
            
#         if pd.api.types.is_numeric_dtype(df[col]):
#             # For numeric: use median for skewed, mean for normal
#             if len(df[col]) > 0:
#                 # Check for suspicious zeros
#                 zero_count = (df[col] == 0).sum()
#                 total_valid = len(df[col]) - missing_count
                
#                 if zero_count > 0 and zero_count < total_valid * 0.3:
#                     # Treat zeros as missing
#                     temp_series = df[col].replace(0, np.nan)
#                     skewness = temp_series.skew()
#                 else:
#                     skewness = df[col].skew()
                
#                 if abs(skewness) > 1:  # Skewed distribution
#                     value = df[col].median()
#                     method = "median"
#                 else:
#                     value = df[col].mean()
#                     method = "mean"
                
#                 df[col] = df[col].fillna(value)
#                 imputations.append(f"{col}: {method}({value:.2f})")
            
#         else:
#             # For categorical: use mode, but handle case when mode is empty
#             if not df[col].mode().empty:
#                 value = df[col].mode()[0]
#                 df[col] = df[col].fillna(value)
#                 imputations.append(f"{col}: mode('{value}')")
#             else:
#                 df[col] = df[col].fillna('Unknown')
#                 imputations.append(f"{col}: 'Unknown'")
    
#     if imputations:
#         logs.append(f"🎯 Smart imputation: {', '.join(imputations)}")
    
#     return df

# def smart_encode_categorical(df, logs):
#     """Smart encoding based on cardinality and data characteristics"""
#     encoded_cols = []
    
#     categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
#     for col in categorical_cols:
#         # Clean data first
#         df[col] = clean_categorical_data(df[col])
#         unique_count = df[col].nunique()
        
#         if unique_count == 2:
#             # Binary encoding
#             le = LabelEncoder()
#             df[col] = le.fit_transform(df[col])
#             encoded_cols.append(f"{col}(binary)")
            
#         elif 2 < unique_count <= 10:
#             # One-hot encoding for low cardinality
#             encoded = pd.get_dummies(df[col], prefix=col, drop_first=True)
#             df = pd.concat([df, encoded], axis=1)
#             df.drop(col, axis=1, inplace=True)
#             encoded_cols.append(f"{col}(one-hot)")
            
#         else:
#             # Label encoding for high cardinality
#             le = LabelEncoder()
#             df[col] = le.fit_transform(df[col])
#             encoded_cols.append(f"{col}(label)")
    
#     if encoded_cols:
#         logs.append(f"🔤 Smart encoding: {', '.join(encoded_cols)}")
    
#     return df

# def smart_handle_outliers(df, logs):
#     """Intelligent outlier handling using multiple methods"""
#     outlier_cols = []
    
#     numeric_cols = df.select_dtypes(include=[np.number]).columns
    
#     for col in numeric_cols:
#         if df[col].nunique() > 2 and df[col].std() > 0:  # Need variation for outlier detection
#             Q1 = df[col].quantile(0.25)
#             Q3 = df[col].quantile(0.75)
#             IQR = Q3 - Q1
            
#             if IQR > 0:
#                 lower_bound = Q1 - 1.5 * IQR
#                 upper_bound = Q3 + 1.5 * IQR
                
#                 outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
                
#                 if outliers > 0:
#                     # Cap outliers instead of removing
#                     df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
#                     df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
#                     outlier_cols.append(f"{col}({outliers} capped)")
    
#     if outlier_cols:
#         logs.append(f"📏 Outlier handling: {', '.join(outlier_cols)}")
    
#     return df

# def smart_scale_features(df, logs):
#     """Intelligent feature scaling based on distribution"""
#     scaled_cols = []
    
#     numeric_cols = df.select_dtypes(include=[np.number]).columns
    
#     for col in numeric_cols:
#         # Only scale if there's variation and no missing values
#         if df[col].nunique() > 1 and df[col].isnull().sum() == 0 and df[col].std() > 0:
#             # Check if scaling is needed (only if range is large)
#             col_range = df[col].max() - df[col].min()
            
#             if col_range > 10:  # Only scale if range is significant
#                 # Use StandardScaler for most cases
#                 scaler = StandardScaler()
#                 df[col] = scaler.fit_transform(df[[col]]).flatten()
#                 scaled_cols.append(f"{col}(standard)")
    
#     if scaled_cols:
#         logs.append(f"⚖️  Smart scaling: {', '.join(scaled_cols)}")
    
#     return df

# def smart_validate_datatypes(df, logs):
#     """Intelligent data type validation and conversion"""
#     conversions = []
    
#     for col in df.columns:
#         if df[col].dtype == 'object':
#             # Try to convert to numeric - be more strict
#             numeric_vals = pd.to_numeric(df[col], errors='coerce')
#             if numeric_vals.notna().sum() > len(df) * 0.95:  # 95% convertible
#                 df[col] = numeric_vals
#                 conversions.append(f"{col}: object→numeric")
            
#             # Convert to categorical if low cardinality
#             elif df[col].nunique() <= 30 and df[col].nunique() > 1:
#                 df[col] = df[col].astype('category')
#                 conversions.append(f"{col}: object→category")
    
#     if conversions:
#         logs.append(f"🔍 Data type optimization: {', '.join(conversions)}")
    
#     return df

# def final_quality_check(df, original_shape):
#     """Comprehensive data quality assessment"""
#     logs = []
    
#     logs.append("📋 FINAL DATA QUALITY REPORT:")
#     logs.append(f"   📊 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
#     # Data quality metrics
#     missing_percent = (df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100
#     logs.append(f"   ✅ Missing Values: {missing_percent:.1f}%")
    
#     duplicate_percent = (df.duplicated().sum() / len(df)) * 100
#     logs.append(f"   ✅ Duplicates: {duplicate_percent:.1f}%")
    
#     # Data type distribution
#     dtype_info = [f"{dtype}({count})" for dtype, count in df.dtypes.value_counts().items()]
#     logs.append(f"   ✅ Data Types: {', '.join(dtype_info)}")
    
#     return logs

# def execute_basic_operation(df, operation, logs):
#     """Fallback for basic operations"""
#     basic_handlers = {
#         "impute:mean": lambda df, logs: df.fillna(df.select_dtypes(include=[np.number]).mean()),
#         "impute:median": lambda df, logs: df.fillna(df.select_dtypes(include=[np.number]).median()),
#         "impute:mode": lambda df, logs: df.fillna(df.select_dtypes(include=['object']).mode().iloc[0]),
#     }
    
#     if operation in basic_handlers:
#         return basic_handlers[operation](df, logs)
#     else:
#         logs.append(f"⚠️  Unknown operation: {operation}")
#         return df

# def get_ai_suggestions(df, logs):
#     """Get preprocessing suggestions from AI"""
#     try:
#         from mainapp.logic.llm_logic import LLMAgent
#         llm = LLMAgent()
#         ai_result = llm.analyze_dataset(df, "column_wise")
        
#         if ai_result.get("status") == "success" and ai_result.get("suggestions"):
#             operations = ai_result.get("suggestions")
#             logs.append(f"🧠 AI suggested: {operations}")
#             return operations
#         else:
#             logs.append("⚠️ No AI suggestions. Using smart defaults.")
#             return ["impute:auto", "validate:datatypes", "encode:categorical"]
            
#     except Exception as e:
#         logs.append(f"⚠️ AI suggestion failed: {str(e)}")
#         return ["impute:auto", "validate:datatypes", "encode:categorical"]

# def save_processed_file(df, original_filename):
#     """Save processed DataFrame"""
#     from mainapp.file.download import save_processed_file as save_file
#     return save_file(df, original_filename)



#################################################################################################






"""
Enhanced Preprocessing Pipeline with Hybrid Rule-Based + LLM-Guided Intelligence
Author: Senior Data Scientist / ML Systems Architect
Version: 2.0
Description: Production-ready preprocessing with domain-realistic validation,
             non-destructive handling, and context-aware intelligence.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, RobustScaler
from sklearn.impute import SimpleImputer, KNNImputer
import warnings
from typing import Dict, List, Tuple, Optional, Any, Set
import logging
from datetime import datetime
from scipy import stats
import json

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Configure logging for production monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Rule-based validation constants
MIN_WORKING_AGE = 16
MAX_HUMAN_AGE = 122  # Oldest verified human age
MIN_PERCENTAGE = 0
MAX_PERCENTAGE = 100
MIN_SALARY = 0  # Could be negative for losses in financial contexts
MAX_REASONABLE_SALARY = 10_000_000  # $10M annual salary threshold

# Domain-specific column patterns for intent inference
AGE_PATTERNS = {'age', 'years', 'years_old', 'dob', 'date_of_birth', 'birth'}
SALARY_PATTERNS = {'salary', 'income', 'wage', 'earnings', 'revenue', 'compensation'}
EXPERIENCE_PATTERNS = {'experience', 'exp', 'years_exp', 'tenure', 'seniority'}
PERCENTAGE_PATTERNS = {'percent', 'percentage', 'rate', 'ratio', 'pct', '_pct'}
COUNT_PATTERNS = {'count', 'number', 'total', 'num_', 'qty', 'quantity'}
DATE_PATTERNS = {'date', 'time', 'datetime', 'timestamp', 'created', 'updated'}
ID_PATTERNS = {'id', 'Id', 'ID', 'uuid', 'guid', 'key', 'code', 'index', 'row_id'}
TARGET_PATTERNS = {'target', 'label', 'class', 'outcome', 'result', 'score', 'rating'}

class RuleValidationEngine:
    """Rule-based validation engine with domain-aware sanity checks"""
    
    def __init__(self):
        self.validation_logs = []
        self.validation_stats = {
            'values_flagged': 0,
            'values_capped': 0,
            'values_marked_missing': 0,
            'columns_skipped': 0
        }
    
    def infer_column_intent(self, col_name: str, series: pd.Series) -> Dict[str, bool]:
        """Infer column intent from name patterns and data distribution"""
        col_name_lower = col_name.lower()
        
        intent = {
            'is_age': False,
            'is_salary': False,
            'is_experience': False,
            'is_percentage': False,
            'is_count': False,
            'is_date': False,
            'is_id': False,
            'is_target': False,
            'confidence': 0.0
        }
        
        # Check name patterns
        name_score = 0
        if any(pattern in col_name_lower for pattern in AGE_PATTERNS):
            intent['is_age'] = True
            name_score += 1
        if any(pattern in col_name_lower for pattern in SALARY_PATTERNS):
            intent['is_salary'] = True
            name_score += 1
        if any(pattern in col_name_lower for pattern in EXPERIENCE_PATTERNS):
            intent['is_experience'] = True
            name_score += 1
        if any(pattern in col_name_lower for pattern in PERCENTAGE_PATTERNS):
            intent['is_percentage'] = True
            name_score += 1
        if any(pattern in col_name_lower for pattern in COUNT_PATTERNS):
            intent['is_count'] = True
            name_score += 1
        if any(pattern in col_name_lower for pattern in DATE_PATTERNS):
            intent['is_date'] = True
            name_score += 1
        if any(pattern in col_name_lower for pattern in ID_PATTERNS):
            intent['is_id'] = True
            name_score += 1
        if any(pattern in col_name_lower for pattern in TARGET_PATTERNS):
            intent['is_target'] = True
            name_score += 1
        
        # Validate with data distribution for numeric columns
        if pd.api.types.is_numeric_dtype(series):
            non_null = series.dropna()
            if len(non_null) > 0:
                data_score = 0
                
                # Age-like distribution check (typically 0-100)
                if intent['is_age'] and (0 <= non_null.median() <= 100):
                    data_score += 1
                
                # Percentage-like distribution (0-100)
                if intent['is_percentage'] and (0 <= non_null.min() <= 100 and 0 <= non_null.max() <= 100):
                    data_score += 1
                
                # Count-like distribution (non-negative integers)
                if intent['is_count'] and (non_null.min() >= 0 and all(non_null == non_null.astype(int))):
                    data_score += 1
                
                # Salary-like distribution (positive values, often right-skewed)
                if intent['is_salary'] and non_null.min() >= 0:
                    data_score += 1
                
                intent['confidence'] = (name_score + data_score) / 2
            else:
                intent['confidence'] = name_score / 1.0
        
        return intent
    
    def validate_age(self, series: pd.Series, col_name: str) -> Tuple[pd.Series, Dict]:
        """Validate age values with domain realism"""
        original_series = series.copy()
        validation_result = {
            'flagged': 0,
            'capped': 0,
            'marked_missing': 0,
            'issues': []
        }
        
        # Skip if not numeric
        if not pd.api.types.is_numeric_dtype(series):
            return series, validation_result
        
        # Create mask for validation
        mask_negative = series < 0
        mask_impossible = series > MAX_HUMAN_AGE
        
        # Handle negative ages - always invalid
        if mask_negative.any():
            n_negative = mask_negative.sum()
            validation_result['issues'].append(f"{n_negative} negative age values")
            
            # Conservative approach: mark as missing with explanation
            series = series.where(~mask_negative, np.nan)
            validation_result['marked_missing'] += n_negative
            validation_result['flagged'] += n_negative
        
        # Handle impossible ages
        if mask_impossible.any():
            n_impossible = mask_impossible.sum()
            validation_result['issues'].append(f"{n_impossible} ages > {MAX_HUMAN_AGE}")
            
            # Cap at maximum reasonable age if only slightly over
            slightly_over = series[series <= MAX_HUMAN_AGE * 1.5]  # Allow some margin
            if len(slightly_over) > 0:
                # Cap extreme values
                series = series.where(~mask_impossible, MAX_HUMAN_AGE)
                validation_result['capped'] += mask_impossible.sum()
            else:
                # Mark as missing if values are completely unreasonable
                series = series.where(~mask_impossible, np.nan)
                validation_result['marked_missing'] += mask_impossible.sum()
            
            validation_result['flagged'] += n_impossible
        
        # Log validation if issues found
        if validation_result['issues']:
            log_msg = f"🔍 Age validation for '{col_name}': {', '.join(validation_result['issues'])}"
            self.validation_logs.append(log_msg)
            self.validation_stats['values_flagged'] += validation_result['flagged']
            self.validation_stats['values_capped'] += validation_result['capped']
            self.validation_stats['values_marked_missing'] += validation_result['marked_missing']
        
        return series, validation_result
    
    def validate_salary(self, series: pd.Series, col_name: str) -> Tuple[pd.Series, Dict]:
        """Validate salary/income values with domain context"""
        validation_result = {
            'flagged': 0,
            'capped': 0,
            'marked_missing': 0,
            'issues': []
        }
        
        if not pd.api.types.is_numeric_dtype(series):
            return series, validation_result
        
        # Negative salaries might be valid in financial contexts (losses)
        # So we only flag, don't automatically correct
        
        # Flag extreme values
        mask_extreme = series > MAX_REASONABLE_SALARY
        if mask_extreme.any():
            n_extreme = mask_extreme.sum()
            validation_result['issues'].append(f"{n_extreme} salaries > ${MAX_REASONABLE_SALARY:,}")
            validation_result['flagged'] += n_extreme
        
        # Log but don't auto-correct - let LLM/analyst decide
        if validation_result['issues']:
            log_msg = f"💰 Salary validation for '{col_name}': {', '.join(validation_result['issues'])}"
            self.validation_logs.append(log_msg)
            self.validation_stats['values_flagged'] += validation_result['flagged']
        
        return series, validation_result
    
    def validate_experience(self, series: pd.Series, col_name: str, age_series: Optional[pd.Series] = None) -> Tuple[pd.Series, Dict]:
        """Validate experience values with logical consistency"""
        validation_result = {
            'flagged': 0,
            'capped': 0,
            'marked_missing': 0,
            'issues': []
        }
        
        if not pd.api.types.is_numeric_dtype(series):
            return series, validation_result
        
        # Basic validation: experience shouldn't be negative
        mask_negative = series < 0
        if mask_negative.any():
            n_negative = mask_negative.sum()
            validation_result['issues'].append(f"{n_negative} negative experience values")
            series = series.where(~mask_negative, np.nan)
            validation_result['marked_missing'] += n_negative
            validation_result['flagged'] += n_negative
        
        # Cross-validation with age if available
        if age_series is not None and pd.api.types.is_numeric_dtype(age_series):
            # Experience should be less than age - MIN_WORKING_AGE
            mask_illogical = (age_series - series) < MIN_WORKING_AGE
            n_illogical = mask_illogical.sum()
            
            if n_illogical > 0:
                validation_result['issues'].append(f"{n_illogical} experience values exceed logical age limits")
                validation_result['flagged'] += n_illogical
                # Don't auto-correct - flag for review
        
        if validation_result['issues']:
            log_msg = f"📊 Experience validation for '{col_name}': {', '.join(validation_result['issues'])}"
            self.validation_logs.append(log_msg)
            self.validation_stats['values_flagged'] += validation_result['flagged']
            self.validation_stats['values_marked_missing'] += validation_result['marked_missing']
        
        return series, validation_result
    
    def validate_percentage(self, series: pd.Series, col_name: str) -> Tuple[pd.Series, Dict]:
        """Validate percentage values (0-100 range)"""
        validation_result = {
            'flagged': 0,
            'capped': 0,
            'marked_missing': 0,
            'issues': []
        }
        
        if not pd.api.types.is_numeric_dtype(series):
            return series, validation_result
        
        # Values below 0% or above 100% are invalid for percentages
        mask_below_zero = series < MIN_PERCENTAGE
        mask_above_max = series > MAX_PERCENTAGE
        
        if mask_below_zero.any():
            n_below = mask_below_zero.sum()
            validation_result['issues'].append(f"{n_below} values < {MIN_PERCENTAGE}%")
            series = series.where(~mask_below_zero, np.nan)
            validation_result['marked_missing'] += n_below
            validation_result['flagged'] += n_below
        
        if mask_above_max.any():
            n_above = mask_above_max.sum()
            validation_result['issues'].append(f"{n_above} values > {MAX_PERCENTAGE}%")
            # Cap at 100% for percentages
            series = series.where(~mask_above_max, MAX_PERCENTAGE)
            validation_result['capped'] += n_above
            validation_result['flagged'] += n_above
        
        if validation_result['issues']:
            log_msg = f"📈 Percentage validation for '{col_name}': {', '.join(validation_result['issues'])}"
            self.validation_logs.append(log_msg)
            self.validation_stats['values_flagged'] += validation_result['flagged']
            self.validation_stats['values_capped'] += validation_result['capped']
            self.validation_stats['values_marked_missing'] += validation_result['marked_missing']
        
        return series, validation_result
    
    def validate_counts(self, series: pd.Series, col_name: str) -> Tuple[pd.Series, Dict]:
        """Validate count values (non-negative integers)"""
        validation_result = {
            'flagged': 0,
            'capped': 0,
            'marked_missing': 0,
            'issues': []
        }
        
        if not pd.api.types.is_numeric_dtype(series):
            return series, validation_result
        
        # Counts should be non-negative
        mask_negative = series < 0
        if mask_negative.any():
            n_negative = mask_negative.sum()
            validation_result['issues'].append(f"{n_negative} negative count values")
            series = series.where(~mask_negative, np.nan)
            validation_result['marked_missing'] += n_negative
            validation_result['flagged'] += n_negative
        
        # Check if values are integers (for count data)
        non_integer_mask = series.dropna().apply(lambda x: not float(x).is_integer())
        if non_integer_mask.any():
            n_non_int = non_integer_mask.sum()
            validation_result['issues'].append(f"{n_non_int} non-integer values in count column")
            validation_result['flagged'] += n_non_int
        
        if validation_result['issues']:
            log_msg = f"🔢 Count validation for '{col_name}': {', '.join(validation_result['issues'])}"
            self.validation_logs.append(log_msg)
            self.validation_stats['values_flagged'] += validation_result['flagged']
            self.validation_stats['values_marked_missing'] += validation_result['marked_missing']
        
        return series, validation_result
    
    def get_validation_summary(self) -> Dict:
        """Get summary of all validation activities"""
        return {
            'logs': self.validation_logs,
            'stats': self.validation_stats,
            'timestamp': datetime.now().isoformat()
        }

class LLMContextAnalyzer:
    """LLM-guided context analysis for intelligent preprocessing decisions"""
    
    def __init__(self, fallback_mode: bool = True):
        self.fallback_mode = fallback_mode
        self.analysis_cache = {}
    
    def analyze_column_context(self, df: pd.DataFrame, col_name: str, rule_engine: RuleValidationEngine) -> Dict:
        """Analyze column context to decide if rules should apply"""
        
        # Check cache
        cache_key = f"{col_name}_{df[col_name].dtype}_{len(df)}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        series = df[col_name]
        intent = rule_engine.infer_column_intent(col_name, series)
        
        analysis = {
            'apply_rules': False,
            'confidence': 0.0,
            'recommended_actions': [],
            'warnings': [],
            'should_preserve': False,
            'intent': intent
        }
        
        # NEVER transform identifier or target columns
        if intent['is_id'] or intent['is_target']:
            analysis['should_preserve'] = True
            analysis['apply_rules'] = False
            analysis['confidence'] = 1.0
            analysis['recommended_actions'] = ['preserve_original']
            self.analysis_cache[cache_key] = analysis
            return analysis
        
        # Analyze data distribution for context
        if pd.api.types.is_numeric_dtype(series):
            non_null = series.dropna()
            if len(non_null) > 0:
                # Check data quality indicators
                missing_pct = series.isnull().sum() / len(series)
                std_dev = non_null.std()
                skewness = non_null.skew()
                
                # High missingness suggests caution
                if missing_pct > 0.3:
                    analysis['warnings'].append(f"High missingness ({missing_pct:.1%}) - apply rules cautiously")
                
                # Zero variance suggests limited utility for some rules
                if std_dev == 0:
                    analysis['warnings'].append("Zero variance - scaling/imputation may not be meaningful")
                
                # Extreme skewness suggests careful outlier handling
                if abs(skewness) > 2:
                    analysis['warnings'].append(f"Highly skewed distribution (skew={skewness:.2f})")
                
                # Determine if rules should apply based on intent confidence
                if intent['confidence'] > 0.7:  # High confidence in intent
                    analysis['apply_rules'] = True
                    analysis['confidence'] = intent['confidence']
                    
                    # Suggest specific actions based on intent
                    if intent['is_age']:
                        analysis['recommended_actions'].extend(['validate_age', 'flag_extremes'])
                    elif intent['is_salary']:
                        analysis['recommended_actions'].extend(['validate_range', 'log_transform_if_skewed'])
                    elif intent['is_percentage']:
                        analysis['recommended_actions'].extend(['validate_percentage', 'cap_extremes'])
                    elif intent['is_count']:
                        analysis['recommended_actions'].extend(['validate_counts', 'consider_poisson'])
                else:
                    # Low confidence - be conservative
                    analysis['apply_rules'] = False
                    analysis['confidence'] = 0.3
                    analysis['warnings'].append(f"Low intent confidence ({intent['confidence']:.2f}) - skipping aggressive rules")
        
        self.analysis_cache[cache_key] = analysis
        return analysis

def run_preprocessing_pipeline(file, operations=None, original_filename=None, column_operations=None):
    """
    Enhanced preprocessing pipeline with hybrid rule-based + LLM intelligence
    """
    logs = []
    download_info = None
    
    # Initialize engines
    rule_engine = RuleValidationEngine()
    llm_analyzer = LLMContextAnalyzer()
    
    try:
        # Step 1: Smart CSV reading with error handling
        df, read_logs = smart_read_csv(file)
        logs.extend(read_logs)

        if df.empty:
            logs.append("❌ Empty dataset loaded")
            return df, logs, None

        original_shape = df.shape
        logs.append(f"✅ Dataset loaded: {original_shape[0]} rows × {original_shape[1]} columns")
        
        # Step 1.5: Apply rule-based validation BEFORE any transformations
        logs.append("🔍 Applying rule-based validation with domain-awareness...")
        df = apply_rule_based_validation(df, rule_engine, logs)
        
        # Log validation summary
        validation_summary = rule_engine.get_validation_summary()
        if validation_summary['logs']:
            logs.extend(validation_summary['logs'])
            logs.append(f"📊 Validation stats: {validation_summary['stats']}")

        # Step 2: Comprehensive data profiling
        profile_logs = enhanced_data_profiling(df, rule_engine)
        logs.extend(profile_logs)

        # Step 3: Use column operations if provided, otherwise get AI suggestions
        if column_operations:
            logs.append(f"🎯 Executing column-wise operations: {column_operations}")
            df = execute_column_wise_operations(df, column_operations, logs, rule_engine, llm_analyzer)
        elif operations:
            logs.append(f"🎯 Executing operations: {operations}")
            df = execute_smart_operations(df, operations, logs, rule_engine, llm_analyzer)
        else:
            operations = get_ai_suggestions_enhanced(df, logs, rule_engine, llm_analyzer)
            logs.append(f"🎯 Executing AI operations: {operations}")
            df = execute_smart_operations(df, operations, logs, rule_engine, llm_analyzer)
        
        # Step 4: Final data quality check
        quality_logs = final_quality_check(df, original_shape)
        logs.extend(quality_logs)

        # Step 5: Save processed file with validation metadata
        if original_filename:
            download_info = save_processed_file_enhanced(df, original_filename, validation_summary)
            logs.append(f"💾 Processed file saved: {download_info['filename']}")

        logs.append("🎉 Preprocessing completed successfully!")
        logs.append("📝 Summary: Rule-based validation + LLM context applied for safe, intelligent preprocessing")

        return df, logs, download_info

    except Exception as e:
        error_msg = f"❌ Preprocessing failed: {str(e)}"
        logs.append(error_msg)
        logger.error(f"Preprocessing error: {str(e)}", exc_info=True)
        return pd.DataFrame(), logs, None

def apply_rule_based_validation(df: pd.DataFrame, rule_engine: RuleValidationEngine, logs: List[str]) -> pd.DataFrame:
    """Apply rule-based validation to all columns with domain awareness"""
    df_validated = df.copy()
    
    # First pass: analyze all columns for intent
    column_intents = {}
    for col in df.columns:
        column_intents[col] = rule_engine.infer_column_intent(col, df[col])
    
    # Second pass: apply appropriate validations
    for col in df.columns:
        intent = column_intents[col]
        
        # Skip non-numeric columns for most validations
        if not pd.api.types.is_numeric_dtype(df[col]):
            continue
        
        # Apply validations based on high-confidence intent
        if intent['is_age'] and intent['confidence'] > 0.6:
            df_validated[col], _ = rule_engine.validate_age(df[col], col)
        
        elif intent['is_salary'] and intent['confidence'] > 0.6:
            df_validated[col], _ = rule_engine.validate_salary(df[col], col)
        
        elif intent['is_experience'] and intent['confidence'] > 0.6:
            # Look for age column for cross-validation
            age_col = None
            for potential_age in df.columns:
                if potential_age != col and column_intents[potential_age]['is_age']:
                    age_col = potential_age
                    break
            age_series = df[age_col] if age_col else None
            df_validated[col], _ = rule_engine.validate_experience(df[col], col, age_series)
        
        elif intent['is_percentage'] and intent['confidence'] > 0.7:
            df_validated[col], _ = rule_engine.validate_percentage(df[col], col)
        
        elif intent['is_count'] and intent['confidence'] > 0.6:
            df_validated[col], _ = rule_engine.validate_counts(df[col], col)
    
    return df_validated

def execute_column_wise_operations(df, column_operations, logs, rule_engine, llm_analyzer):
    """Execute column-wise operations with LLM context awareness"""
    executed_ops = []
    
    # Handle dataset-wide operations first
    if "dataset_wide" in column_operations:
        for operation in column_operations["dataset_wide"]:
            df = execute_single_operation_enhanced(df, operation, "dataset_wide", logs, rule_engine, llm_analyzer)
            executed_ops.append(f"dataset_wide:{operation}")
    
    # Handle column-specific operations with context analysis
    for column, operations in column_operations.items():
        if column == "dataset_wide":
            continue
            
        if column not in df.columns:
            logs.append(f"⚠️  Column '{column}' not found in dataset. Skipping operations.")
            continue
        
        # Analyze column context before applying operations
        context = llm_analyzer.analyze_column_context(df, column, rule_engine)
        
        # Skip operations on identifier/target columns
        if context['should_preserve']:
            logs.append(f"🛡️  Skipping operations on identifier/target column: '{column}'")
            continue
        
        # Apply warnings from context analysis
        if context['warnings']:
            logs.append(f"⚠️  Context warnings for '{column}': {', '.join(context['warnings'])}")
        
        for operation in operations:
            # Check if operation should be applied based on context
            if not context['apply_rules'] and operation.startswith(('validate:', 'handle:', 'scale:')):
                logs.append(f"⏸️  Skipping rule-based operation '{operation}' on '{column}' (low confidence)")
                continue
            
            df = execute_single_operation_enhanced(df, operation, column, logs, rule_engine, llm_analyzer)
            executed_ops.append(f"{column}:{operation}")
    
    if executed_ops:
        logs.append(f"✅ Executed column operations: {executed_ops}")
    
    return df

def execute_single_operation_enhanced(df, operation, column, logs, rule_engine, llm_analyzer):
    """Enhanced single operation execution with safety checks"""
    try:
        if column == "dataset_wide":
            # Dataset-wide operations
            if operation == "remove:duplicates":
                initial_count = len(df)
                df = df.drop_duplicates()
                removed = initial_count - len(df)
                if removed > 0:
                    logs.append(f"🧹 Removed {removed} duplicate rows ({removed/initial_count*100:.1f}%)")
            
            elif operation == "validate:datatypes":
                conversions = smart_validate_datatypes_enhanced(df, logs, rule_engine)
                if conversions:
                    logs.append(f"🔍 Data type validation: {', '.join(conversions)}")
        
        else:
            # Column-specific operations with enhanced safety
            if operation.startswith("impute:"):
                df = safe_imputation(df, column, operation, logs, rule_engine)
            
            elif operation.startswith("scale:"):
                df = safe_scaling(df, column, operation, logs, llm_analyzer)
            
            elif operation == "handle:outliers":
                df = safe_outlier_handling(df, column, logs, llm_analyzer)
            
            elif operation.startswith("encode:"):
                df = safe_encoding(df, column, operation, logs, rule_engine)
            
            elif operation == "clean:text":
                df = safe_text_cleaning(df, column, logs)
            
            elif operation == "drop:column":
                df = safe_column_dropping(df, column, logs, rule_engine)
            
            elif operation == "log_transform":
                df = safe_log_transform(df, column, logs, llm_analyzer)
        
        return df
        
    except Exception as e:
        logs.append(f"⚠️  Operation '{operation}' on '{column}' failed: {str(e)}")
        logger.warning(f"Operation failed: {operation} on {column}", exc_info=True)
        return df

def safe_imputation(df, column, operation, logs, rule_engine):
    """Safe imputation with domain awareness"""
    if column not in df.columns:
        return df
    
    # Analyze column intent
    intent = rule_engine.infer_column_intent(column, df[column])
    
    missing_count = df[column].isnull().sum()
    if missing_count == 0:
        return df
    
    # Handle different imputation strategies
    if operation == "impute:mean":
        if pd.api.types.is_numeric_dtype(df[column]):
            # Check if mean is appropriate
            if intent['is_count']:
                logs.append(f"⚠️  Using median instead of mean for count column '{column}'")
                impute_value = df[column].median()
            else:
                impute_value = df[column].mean()
            
            df[column] = df[column].fillna(impute_value)
            logs.append(f"📊 {column}: imputed {missing_count} values with {operation.split(':')[1]} ({impute_value:.2f})")
    
    elif operation == "impute:median":
        if pd.api.types.is_numeric_dtype(df[column]):
            impute_value = df[column].median()
            df[column] = df[column].fillna(impute_value)
            logs.append(f"📊 {column}: imputed {missing_count} values with median ({impute_value:.2f})")
    
    elif operation == "impute:mode":
        if pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_categorical_dtype(df[column]):
            clean_series = clean_categorical_data(df[column])
            if not clean_series.mode().empty:
                impute_value = clean_series.mode()[0]
                df[column] = clean_series.fillna(impute_value)
                logs.append(f"🏷️  {column}: imputed {missing_count} values with mode ('{impute_value}')")
            else:
                df[column] = clean_series.fillna('Unknown')
                logs.append(f"🏷️  {column}: imputed {missing_count} values with 'Unknown'")
    
    elif operation == "impute:knn":
        if pd.api.types.is_numeric_dtype(df[column]):
            # Use KNN imputation for numeric columns
            try:
                from sklearn.impute import KNNImputer
                imputer = KNNImputer(n_neighbors=5)
                # Impute only this column (simplified approach)
                temp_df = df[[column]].copy()
                temp_df[column] = imputer.fit_transform(temp_df)
                df[column] = temp_df[column]
                logs.append(f"🤖 {column}: KNN imputation applied to {missing_count} values")
            except:
                # Fallback to median
                impute_value = df[column].median()
                df[column] = df[column].fillna(impute_value)
                logs.append(f"📊 {column}: KNN failed, used median ({impute_value:.2f})")
    
    return df

def safe_scaling(df, column, operation, logs, llm_analyzer):
    """Safe scaling with distribution awareness"""
    if column not in df.columns:
        return df
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        logs.append(f"⚠️  Cannot scale non-numeric column '{column}'")
        return df
    
    # Check preconditions
    if df[column].nunique() <= 1:
        logs.append(f"⚠️  Skipping scaling for constant column '{column}'")
        return df
    
    if df[column].isnull().any():
        logs.append(f"⚠️  Skipping scaling for column with missing values '{column}'")
        return df
    
    # Analyze context
    context = llm_analyzer.analyze_column_context(df, column, RuleValidationEngine())
    
    # Apply scaling based on operation and context
    if operation == "scale:standard":
        if context['intent']['is_percentage']:
            logs.append(f"⚠️  Standard scaling may not be appropriate for percentages '{column}'")
        
        scaler = StandardScaler()
        df[column] = scaler.fit_transform(df[[column]]).flatten()
        logs.append(f"⚖️  {column}: standardized scaling applied")
    
    elif operation == "scale:minmax":
        scaler = MinMaxScaler()
        df[column] = scaler.fit_transform(df[[column]]).flatten()
        logs.append(f"⚖️  {column}: min-max scaling applied (0-1 range)")
    
    elif operation == "scale:robust":
        # Robust scaling for columns with outliers
        scaler = RobustScaler()
        df[column] = scaler.fit_transform(df[[column]]).flatten()
        logs.append(f"⚖️  {column}: robust scaling applied (outlier-resistant)")
    
    return df

def safe_outlier_handling(df, column, logs, llm_analyzer):
    """Safe outlier handling with multiple detection methods"""
    if column not in df.columns:
        return df
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return df
    
    # Analyze context
    context = llm_analyzer.analyze_column_context(df, column, RuleValidationEngine())
    
    # Skip if identified as ID or target
    if context['should_preserve']:
        return df
    
    # Multiple outlier detection methods
    methods_applied = []
    
    # Method 1: IQR-based detection (conservative)
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    if IQR > 0:
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers_iqr = ((df[column] < lower_bound) | (df[column] > upper_bound)).sum()
        if outliers_iqr > 0:
            # Cap instead of remove
            df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
            df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
            methods_applied.append(f"IQR-capped({outliers_iqr})")
    
    # Method 2: Z-score based detection for extreme outliers only
    z_scores = np.abs(stats.zscore(df[column].dropna()))
    if len(z_scores) > 0:
        extreme_mask = z_scores > 3.5  # Very conservative threshold
        outliers_z = extreme_mask.sum()
        
        if outliers_z > 0:
            methods_applied.append(f"Z-flagged({outliers_z})")
            # Just flag, don't auto-correct for extreme z-scores
    
    if methods_applied:
        logs.append(f"📏 {column}: outlier handling applied [{', '.join(methods_applied)}]")
    
    return df

def safe_log_transform(df, column, logs, llm_analyzer):
    """Safe log transformation for highly skewed data"""
    if column not in df.columns:
        return df
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        return df
    
    # Check for negative values
    if (df[column] <= 0).any():
        logs.append(f"⚠️  Cannot apply log transform to non-positive values in '{column}'")
        return df
    
    # Check skewness
    skewness = df[column].skew()
    if abs(skewness) < 1:  # Not skewed enough
        logs.append(f"⚠️  Column '{column}' not sufficiently skewed (skew={skewness:.2f}) for log transform")
        return df
    
    # Apply log transform
    df[column] = np.log1p(df[column])  # log(1+x) to handle zeros
    logs.append(f"📈 {column}: log transform applied (original skew={skewness:.2f})")
    
    return df

def safe_encoding(df, column, operation, logs, rule_engine):
    """Safe encoding for categorical data"""
    if column not in df.columns:
        return df
    
    # Check if column should be preserved
    intent = rule_engine.infer_column_intent(column, df[column])
    if intent['is_id'] or intent['is_target']:
        logs.append(f"🛡️  Skipping encoding on identifier/target column: '{column}'")
        return df
    
    if not (pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_categorical_dtype(df[column])):
        logs.append(f"⚠️  Cannot encode non-categorical column '{column}'")
        return df
    
    # Clean data first
    df[column] = clean_categorical_data(df[column])
    unique_count = df[column].nunique()
    
    if operation == "encode:onehot":
        if 1 < unique_count <= 15:  # Reasonable limit for one-hot
            # Use proper one-hot encoding
            encoded = pd.get_dummies(df[column], prefix=column, drop_first=True)
            df = pd.concat([df, encoded], axis=1)
            df.drop(column, axis=1, inplace=True)
            logs.append(f"🔤 {column}: one-hot encoded into {len(encoded.columns)} columns")
        else:
            logs.append(f"⚠️  {column}: unsuitable for one-hot encoding ({unique_count} categories)")
    
    elif operation == "encode:label":
        if unique_count > 1:
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column].astype(str))
            logs.append(f"🔤 {column}: label encoded ({len(le.classes_)} categories)")
    
    return df

def safe_text_cleaning(df, column, logs):
    """Safe text cleaning for categorical/text columns"""
    if column not in df.columns:
        return df
    
    if pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_string_dtype(df[column]):
        original_sample = df[column].iloc[0] if len(df[column]) > 0 else ""
        df[column] = clean_categorical_data(df[column])
        new_sample = df[column].iloc[0] if len(df[column]) > 0 else ""
        
        if original_sample != new_sample:
            logs.append(f"🧹 {column}: text cleaning applied")
    
    return df

def safe_column_dropping(df, column, logs, rule_engine):
    """Safe column dropping with validation"""
    if column not in df.columns:
        logs.append(f"⚠️  Column '{column}' not found for dropping")
        return df
    
    # Check if column should be preserved
    intent = rule_engine.infer_column_intent(column, df[column])
    if intent['is_id']:
        logs.append(f"🛡️  Skipping drop on identifier column: '{column}'")
        return df
    
    df.drop(column, axis=1, inplace=True)
    logs.append(f"🗑️  {column}: column dropped")
    
    return df

def enhanced_data_profiling(df, rule_engine):
    """Enhanced data profiling with domain intent analysis"""
    logs = []
    
    logs.append(f"📊 Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Missing values analysis
    missing_stats = df.isnull().sum()
    total_missing = missing_stats.sum()
    missing_percent = (total_missing / (df.shape[0] * df.shape[1])) * 100
    
    logs.append(f"🔍 Missing Values: {total_missing} total ({missing_percent:.1f}%)")
    
    if total_missing > 0:
        high_missing = missing_stats[missing_stats > 0].sort_values(ascending=False)
        missing_info = []
        for col, count in high_missing.items():
            intent = rule_engine.infer_column_intent(col, df[col])
            if intent['confidence'] > 0.6:
                missing_info.append(f"{col}({count}, {list(k for k,v in intent.items() if v and k != 'confidence')})")
            else:
                missing_info.append(f"{col}({count})")
        
        if missing_info:
            logs.append(f"   Columns with missing values: {', '.join(missing_info[:10])}")
            if len(missing_info) > 10:
                logs.append(f"   ... and {len(missing_info) - 10} more")
    
    # Data types with intent analysis
    dtype_counts = df.dtypes.value_counts()
    logs.append(f"📈 Data Types: {', '.join([f'{dtype}({count})' for dtype, count in dtype_counts.items()])}")
    
    # Column intent summary
    intent_summary = {}
    for col in df.columns:
        intent = rule_engine.infer_column_intent(col, df[col])
        for intent_type, has_intent in intent.items():
            if has_intent and intent_type != 'confidence':
                intent_summary.setdefault(intent_type, 0)
                intent_summary[intent_type] += 1
    
    if intent_summary:
        logs.append(f"🎯 Inferred column intents: {', '.join([f'{k}({v})' for k, v in intent_summary.items()])}")
    
    # Duplicate analysis
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        logs.append(f"⚠️  Duplicate Rows: {duplicate_count} ({duplicate_count/len(df)*100:.1f}%)")
    
    return logs

def smart_validate_datatypes_enhanced(df, logs, rule_engine):
    """Enhanced data type validation with intent awareness"""
    conversions = []
    
    for col in df.columns:
        current_dtype = df[col].dtype
        
        # NEVER convert ID or target columns
        intent = rule_engine.infer_column_intent(col, df[col])
        if intent['is_id'] or intent['is_target']:
            continue
        
        if current_dtype == 'object':
            # Try to convert to numeric - with intent awareness
            numeric_vals = pd.to_numeric(df[col], errors='coerce')
            numeric_count = numeric_vals.notna().sum()
            
            # Determine conversion threshold based on intent
            if intent['confidence'] > 0.7:
                threshold = 0.8  # Higher confidence allows more aggressive conversion
            else:
                threshold = 0.95  # Be conservative
            
            if numeric_count > len(df) * threshold:
                df[col] = numeric_vals
                conversions.append(f"{col}: object→numeric")
            
            # Convert to categorical based on cardinality and intent
            unique_count = df[col].nunique()
            if 1 < unique_count <= 50:  # Reasonable categorical limit
                if not intent['is_age'] and not intent['is_salary']:  # Don't categorize obvious numeric columns
                    df[col] = df[col].astype('category')
                    conversions.append(f"{col}: object→category")
    
    return conversions

def get_ai_suggestions_enhanced(df, logs, rule_engine, llm_analyzer):
    """Enhanced AI suggestions with rule-based constraints"""
    try:
        from mainapp.logic.llm_logic import LLMAgent
        llm = LLMAgent()
        
        # Provide rule-based context to AI
        rule_context = {}
        for col in df.columns:
            intent = rule_engine.infer_column_intent(col, df[col])
            context = llm_analyzer.analyze_column_context(df, col, rule_engine)
            rule_context[col] = {
                'intent': intent,
                'context': context,
                'dtype': str(df[col].dtype),
                'missing_pct': df[col].isnull().sum() / len(df),
                'unique_count': df[col].nunique()
            }
        
        ai_result = llm.analyze_dataset(df, "column_wise", rule_context=rule_context)
        
        if ai_result.get("status") == "success" and ai_result.get("suggestions"):
            operations = ai_result.get("suggestions")
            
            # Filter operations based on rule constraints
            filtered_operations = []
            for op in operations:
                if isinstance(op, dict) and 'column' in op:
                    # Column-specific operation
                    col = op['column']
                    if col in df.columns:
                        context = llm_analyzer.analyze_column_context(df, col, rule_engine)
                        if not context['should_preserve']:
                            filtered_operations.append(op)
                else:
                    # Dataset-wide operation
                    filtered_operations.append(op)
            
            logs.append(f"🧠 AI suggested (filtered by rules): {filtered_operations}")
            return filtered_operations
        else:
            logs.append("⚠️ No AI suggestions. Using smart defaults with rule constraints.")
            return get_safe_default_operations(df, rule_engine)
            
    except Exception as e:
        logs.append(f"⚠️ AI suggestion failed: {str(e)}. Using safe defaults.")
        return get_safe_default_operations(df, rule_engine)

def get_safe_default_operations(df, rule_engine):
    """Get safe default operations respecting rule constraints"""
    operations = ["validate:datatypes"]
    
    # Add imputation only if needed
    missing_cols = [col for col in df.columns if df[col].isnull().any()]
    if missing_cols:
        operations.append("impute:auto")
    
    # Add encoding only for appropriate columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    safe_categorical_cols = []
    for col in categorical_cols:
        intent = rule_engine.infer_column_intent(col, df[col])
        if not intent['is_id'] and not intent['is_target']:
            safe_categorical_cols.append(col)
    
    if len(safe_categorical_cols) > 0:
        operations.append("encode:categorical")
    
    return operations

def save_processed_file_enhanced(df, original_filename, validation_summary):
    """Save processed file with validation metadata"""
    from mainapp.file.download import save_processed_file as save_file
    
    # Add validation metadata as comment in saved file
    metadata = {
        'validation_summary': validation_summary,
        'processed_timestamp': datetime.now().isoformat(),
        'original_filename': original_filename,
        'processed_shape': df.shape
    }
    
    # Save metadata as JSON in a separate file or as comment
    import os
    metadata_filename = f"{os.path.splitext(original_filename)[0]}_validation_metadata.json"
    
    # In production, you might save this to a database or metadata store
    # For now, we'll just include it in the return info
    
    download_info = save_file(df, original_filename)
    download_info['validation_metadata'] = metadata
    
    return download_info

# Keep existing helper functions but add safety checks
def clean_categorical_data(series):
    """Clean and standardize categorical data with maximum accuracy"""
    # Preserve original for reference
    original_series = series.copy()
    
    # Handle missing values first
    series = series.fillna('Unknown')
    
    # Convert to string
    series = series.astype(str)
    
    # Replace various null representations
    null_patterns = ['nan', 'None', 'NULL', 'null', 'NaN', 'none', '']
    series = series.replace(null_patterns, 'Unknown')
    
    # Standardize text: trim, lowercase, remove extra spaces
    series = series.str.strip()
    
    # Don't lowercase if it might be case-sensitive (like IDs)
    if not any(pattern in str(series.name).lower() for pattern in ID_PATTERNS):
        series = series.str.lower()
    
    series = series.str.replace(r'\s+', ' ', regex=True)
    
    # Special handling for gender-like columns
    if series.name and ('gender' in str(series.name).lower() or 'sex' in str(series.name).lower()):
        series = series.replace({
            'm': 'male', 'male': 'male', 'male.': 'male',
            'f': 'female', 'female': 'female', 'female.': 'female',
            'unknown': 'unknown'
        })
    
    # Special handling for name columns (don't modify names too much)
    if series.name and 'name' in str(series.name).lower():
        # Just capitalize first letter of each word
        series = series.str.title()
    elif not any(pattern in str(series.name).lower() for pattern in ID_PATTERNS):
        # For other categorical data, capitalize first letter (except IDs)
        series = series.str.title()
    
    # Log if significant changes were made (excluding null handling)
    changes = (original_series.fillna('Unknown') != series).sum()
    if changes > 0:
        logger.info(f"Cleaned categorical data for {series.name}: {changes} values modified")
    
    return series

# Update existing functions to use enhanced versions
def execute_smart_operations(df, operations, logs, rule_engine, llm_analyzer):
    """Execute operations with rule and context awareness"""
    # Map to enhanced handlers
    operation_handlers = {
        "remove:duplicates": smart_remove_duplicates,
        "validate:datatypes": lambda df, logs: smart_validate_datatypes_enhanced(df, logs, rule_engine),
        "impute:auto": lambda df, logs: smart_impute_auto_enhanced(df, logs, rule_engine),
        "encode:categorical": smart_encode_categorical,
        "handle:outliers": lambda df, logs: smart_handle_outliers_enhanced(df, logs, llm_analyzer),
        "scale:auto": lambda df, logs: smart_scale_features_enhanced(df, logs, llm_analyzer),
    }
    
    for operation in operations:
        try:
            if operation in operation_handlers:
                df = operation_handlers[operation](df, logs)
            else:
                # Fallback to enhanced basic operation
                df = execute_basic_operation_enhanced(df, operation, logs, rule_engine)
        except Exception as e:
            logs.append(f"⚠️  Operation '{operation}' skipped: {str(e)}")
            logger.warning(f"Operation skipped: {operation}", exc_info=True)
            continue
    
    return df

def smart_remove_duplicates(df, logs):
    """Smart duplicate removal with analysis"""
    initial_count = len(df)
    df = df.drop_duplicates()
    removed = initial_count - len(df)
    if removed > 0:
        logs.append(f"🧹 Removed {removed} duplicate rows ({removed/initial_count*100:.1f}%)")
    return df

def smart_encode_categorical(df, logs):
    """Smart encoding based on cardinality and data characteristics"""
    encoded_cols = []
    
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    for col in categorical_cols:
        # Clean data first
        df[col] = clean_categorical_data(df[col])
        unique_count = df[col].nunique()
        
        if unique_count == 2:
            # Binary encoding
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoded_cols.append(f"{col}(binary)")
            
        elif 2 < unique_count <= 10:
            # One-hot encoding for low cardinality
            encoded = pd.get_dummies(df[col], prefix=col, drop_first=True)
            df = pd.concat([df, encoded], axis=1)
            df.drop(col, axis=1, inplace=True)
            encoded_cols.append(f"{col}(one-hot)")
            
        else:
            # Label encoding for high cardinality
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoded_cols.append(f"{col}(label)")
    
    if encoded_cols:
        logs.append(f"🔤 Smart encoding: {', '.join(encoded_cols)}")
    
    return df

def smart_impute_auto_enhanced(df, logs, rule_engine):
    """Enhanced intelligent imputation with domain awareness"""
    imputations = []
    
    for col in df.columns:
        missing_count = df[col].isnull().sum()
        
        if missing_count == 0:
            continue
        
        # Check if column should be preserved
        intent = rule_engine.infer_column_intent(col, df[col])
        if intent['is_id'] or intent['is_target']:
            continue
        
        if pd.api.types.is_numeric_dtype(df[col]):
            # Domain-aware imputation strategy
            if intent['is_age']:
                # For ages, use median (robust to outliers)
                value = df[col].median()
                method = "median (age-aware)"
            elif intent['is_count']:
                # For counts, use median and round to integer
                value = round(df[col].median())
                method = "median-rounded (count-aware)"
            elif intent['is_percentage']:
                # For percentages, use median capped at 0-100
                value = max(0, min(100, df[col].median()))
                method = "median-capped (percentage-aware)"
            else:
                # Default: use median for skewed, mean for normal
                skewness = df[col].skew()
                if abs(skewness) > 1:
                    value = df[col].median()
                    method = "median (skewed)"
                else:
                    value = df[col].mean()
                    method = "mean (normal)"
            
            df[col] = df[col].fillna(value)
            imputations.append(f"{col}: {method}({value:.2f})")
        
        else:
            # For categorical: use mode, but handle carefully
            clean_series = clean_categorical_data(df[col])
            if not clean_series.mode().empty:
                value = clean_series.mode()[0]
                df[col] = clean_series.fillna(value)
                imputations.append(f"{col}: mode('{value}')")
            else:
                df[col] = clean_series.fillna('Unknown')
                imputations.append(f"{col}: 'Unknown'")
    
    if imputations:
        logs.append(f"🎯 Smart imputation: {', '.join(imputations[:10])}")
        if len(imputations) > 10:
            logs.append(f"   ... and {len(imputations) - 10} more columns imputed")
    
    return df

def smart_handle_outliers_enhanced(df, logs, llm_analyzer):
    """Enhanced outlier handling with context awareness"""
    outlier_cols = []
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        # Analyze context
        context = llm_analyzer.analyze_column_context(df, col, RuleValidationEngine())
        
        # Skip ID/target columns
        if context['should_preserve']:
            continue
        
        # Skip if no variation
        if df[col].nunique() <= 2 or df[col].std() == 0:
            continue
        
        # Apply appropriate outlier handling based on intent
        if context['intent']['is_age']:
            # For ages, use conservative IQR with biological constraints
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            if IQR > 0:
                lower_bound = max(0, Q1 - 1.5 * IQR)  # Age can't be negative
                upper_bound = min(MAX_HUMAN_AGE, Q3 + 1.5 * IQR)  # Biological limit
                
                outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
                
                if outliers > 0:
                    # Cap with biological constraints
                    df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
                    df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
                    outlier_cols.append(f"{col}({outliers} capped, age-aware)")
        
        elif context['intent']['is_percentage']:
            # For percentages, cap at 0-100
            outliers_below = (df[col] < 0).sum()
            outliers_above = (df[col] > 100).sum()
            
            if outliers_below > 0 or outliers_above > 0:
                df[col] = np.where(df[col] < 0, 0, df[col])
                df[col] = np.where(df[col] > 100, 100, df[col])
                outlier_cols.append(f"{col}({outliers_below + outliers_above} capped, 0-100%)")
        
        else:
            # Default IQR-based handling
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            if IQR > 0:
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
                
                if outliers > 0:
                    # Cap outliers
                    df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
                    df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
                    outlier_cols.append(f"{col}({outliers} capped)")
    
    if outlier_cols:
        logs.append(f"📏 Enhanced outlier handling: {', '.join(outlier_cols[:10])}")
        if len(outlier_cols) > 10:
            logs.append(f"   ... and {len(outlier_cols) - 10} more columns processed")
    
    return df

def smart_scale_features_enhanced(df, logs, llm_analyzer):
    """Enhanced feature scaling with distribution awareness"""
    scaled_cols = []
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        # Check preconditions
        if df[col].nunique() <= 1 or df[col].isnull().any() or df[col].std() == 0:
            continue
        
        # Analyze context
        context = llm_analyzer.analyze_column_context(df, col, RuleValidationEngine())
        
        # Skip ID/target columns
        if context['should_preserve']:
            continue
        
        # Choose scaling method based on distribution and intent
        skewness = df[col].skew()
        
        if context['intent']['is_percentage']:
            # Percentages often don't need scaling
            if df[col].max() <= 100 and df[col].min() >= 0:
                scaled_cols.append(f"{col}(skipped - already 0-100%)")
                continue
        
        if abs(skewness) > 2:
            # Highly skewed - use RobustScaler or consider log transform first
            scaler = RobustScaler()
            df[col] = scaler.fit_transform(df[[col]]).flatten()
            scaled_cols.append(f"{col}(robust, skew={skewness:.2f})")
        elif context['intent']['is_age'] or context['intent']['is_count']:
            # For age/count, use MinMaxScaler to preserve interpretability
            scaler = MinMaxScaler()
            df[col] = scaler.fit_transform(df[[col]]).flatten()
            scaled_cols.append(f"{col}(minmax)")
        else:
            # Default: StandardScaler
            scaler = StandardScaler()
            df[col] = scaler.fit_transform(df[[col]]).flatten()
            scaled_cols.append(f"{col}(standard)")
    
    if scaled_cols:
        logs.append(f"⚖️  Enhanced scaling: {', '.join(scaled_cols[:10])}")
        if len(scaled_cols) > 10:
            logs.append(f"   ... and {len(scaled_cols) - 10} more columns scaled")
    
    return df

def execute_basic_operation_enhanced(df, operation, logs, rule_engine):
    """Enhanced fallback for basic operations with safety checks"""
    basic_handlers = {
        "impute:mean": lambda df, logs: safe_fillna(df, df.select_dtypes(include=[np.number]).mean(), "mean"),
        "impute:median": lambda df, logs: safe_fillna(df, df.select_dtypes(include=[np.number]).median(), "median"),
        "impute:mode": lambda df, logs: safe_fillna(df, df.select_dtypes(include=['object']).mode().iloc[0], "mode"),
    }
    
    if operation in basic_handlers:
        return basic_handlers[operation](df, logs)
    else:
        logs.append(f"⚠️  Unknown operation: {operation}")
        return df

def safe_fillna(df, fill_values, method_name):
    """Safely fill NA values, skipping ID/target columns"""
    df_filled = df.copy()
    
    for col in fill_values.index:
        if col in df.columns:
            # Simple check - in production, use RuleValidationEngine
            if not any(pattern in str(col).lower() for pattern in ID_PATTERNS + tuple(TARGET_PATTERNS)):
                df_filled[col] = df[col].fillna(fill_values[col])
    
    return df_filled

def smart_read_csv(file):
    """Intelligent CSV reading with maximum accuracy"""
    logs = []
    try:
        if isinstance(file, str):
            df = pd.read_csv(file)
        else:
            df = pd.read_csv(file)
        
        # Auto-detect and fix common CSV issues
        df = fix_common_csv_issues(df, logs)
        
        logs.append("✅ CSV read successfully with auto-correction")
        return df, logs
        
    except Exception as e:
        logs.append(f"❌ Failed to read CSV: {str(e)}")
        logger.error(f"CSV read error: {str(e)}", exc_info=True)
        return pd.DataFrame(), logs

def fix_common_csv_issues(df, logs):
    """Fix common CSV parsing issues with maximum accuracy"""
    fixes = []
    
    # Remove extra spaces from column names
    original_cols = df.columns.tolist()
    df.columns = df.columns.str.strip()
    if original_cols != df.columns.tolist():
        fixes.append("trimmed column spaces")
    
    # Convert common null representations to actual NaN
    null_patterns = ['Null', 'null', 'NA', 'N/A', 'NaN', 'nan', 'None', 'none', '']
    null_count = df.isin(null_patterns).sum().sum()
    if null_count > 0:
        df.replace(null_patterns, np.nan, inplace=True)
        fixes.append(f"converted {null_count} text nulls to NaN")
    
    # Auto-detect numeric columns stored as objects
    numeric_conversions = []
    for col in df.select_dtypes(include=['object']).columns:
        # Skip columns that look like IDs
        if any(pattern in str(col).lower() for pattern in ID_PATTERNS):
            continue
        
        # Try to convert to numeric
        numeric_vals = pd.to_numeric(df[col], errors='coerce')
        non_null_count = numeric_vals.notna().sum()
        
        # More conservative conversion
        if non_null_count > len(df) * 0.9:  # 90% convertible
            df[col] = numeric_vals
            numeric_conversions.append(col)
    
    if numeric_conversions:
        fixes.append(f"auto-converted to numeric: {numeric_conversions}")
    
    if fixes:
        logs.append(f"🔧 Auto-fixes applied: {', '.join(fixes)}")
    
    return df

def final_quality_check(df, original_shape):
    """Comprehensive data quality assessment with rule-based insights"""
    logs = []
    
    logs.append("📋 FINAL DATA QUALITY REPORT:")
    logs.append(f"   📊 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Data quality metrics
    missing_percent = (df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100
    logs.append(f"   ✅ Missing Values: {missing_percent:.1f}%")
    
    duplicate_percent = (df.duplicated().sum() / len(df)) * 100
    logs.append(f"   ✅ Duplicates: {duplicate_percent:.1f}%")
    
    # Data type distribution
    dtype_info = [f"{dtype}({count})" for dtype, count in df.dtypes.value_counts().items()]
    logs.append(f"   ✅ Data Types: {', '.join(dtype_info)}")
    
    # Check for any columns with all identical values (no information)
    constant_cols = []
    for col in df.columns:
        if df[col].nunique() == 1:
            constant_cols.append(col)
    
    if constant_cols:
        logs.append(f"   ⚠️  Constant columns (no variation): {', '.join(constant_cols[:5])}")
        if len(constant_cols) > 5:
            logs.append(f"      ... and {len(constant_cols) - 5} more")
    
    # Check for high-cardinality categorical columns
    high_card_cols = []
    for col in df.select_dtypes(include=['object', 'category']).columns:
        if df[col].nunique() > 50:
            high_card_cols.append((col, df[col].nunique()))
    
    if high_card_cols:
        logs.append(f"   ⚠️  High-cardinality categorical columns:")
        for col, count in high_card_cols[:3]:
            logs.append(f"      {col}: {count} unique values")
        if len(high_card_cols) > 3:
            logs.append(f"      ... and {len(high_card_cols) - 3} more")
    
    return logs

# Backward compatibility functions
def execute_single_operation(df, operation, column, logs):
    """Legacy function for backward compatibility"""
    logger.warning("Using legacy execute_single_operation - consider upgrading to enhanced version")
    # Initialize engines for compatibility
    rule_engine = RuleValidationEngine()
    llm_analyzer = LLMContextAnalyzer()
    return execute_single_operation_enhanced(df, operation, column, logs, rule_engine, llm_analyzer)

def data_profiling(df):
    """Legacy data profiling for backward compatibility"""
    logger.warning("Using legacy data_profiling - consider upgrading to enhanced version")
    rule_engine = RuleValidationEngine()
    return enhanced_data_profiling(df, rule_engine)

def analyze_column(series, col_name):
    """Legacy column analysis for backward compatibility"""
    logs = []
    dtype = series.dtype
    missing = series.isnull().sum()
    unique_count = series.nunique()
    
    logs.append(f"   📍 {col_name}: {dtype}, {missing} missing, {unique_count} unique")
    
    if pd.api.types.is_numeric_dtype(series):
        if len(series) > 0:
            # Check for suspicious zeros
            zero_count = (series == 0).sum()
            total_non_missing = len(series) - missing
            
            if zero_count > 0:
                zero_percent = (zero_count / total_non_missing) * 100
                if zero_percent < 50:  # If less than 50% zeros, they might be invalid
                    logs.append(f"      ⚠️  Contains {zero_count} suspicious zero values ({zero_percent:.1f}%)")
                else:
                    logs.append(f"      📊 Contains {zero_count} zero values ({zero_percent:.1f}%)")
            
            if missing == 0 and total_non_missing > 0:
                stats = f"min={series.min():.2f}, max={series.max():.2f}, mean={series.mean():.2f}, std={series.std():.2f}"
                logs.append(f"      📊 {stats}")
                
                # Check for potential outliers
                if series.std() > 0:
                    Q1 = series.quantile(0.25)
                    Q3 = series.quantile(0.75)
                    IQR = Q3 - Q1
                    if IQR > 0:
                        lower_bound = Q1 - 1.5 * IQR
                        upper_bound = Q3 + 1.5 * IQR
                        outliers = ((series < lower_bound) | (series > upper_bound)).sum()
                        if outliers > 0:
                            logs.append(f"      📏 Potential outliers: {outliers}")
    
    elif pd.api.types.is_string_dtype(series) or pd.api.types.is_object_dtype(series):
        if unique_count <= 20:
            top_values = series.value_counts().head(3)
            top_info = [f"{val}({count})" for val, count in top_values.items()]
            logs.append(f"      🏷️  Top values: {', '.join(top_info)}")
        else:
            logs.append(f"      🔤 High cardinality: {unique_count} categories")
    
    return logs

def get_ai_suggestions(df, logs):
    """Legacy AI suggestions for backward compatibility"""
    logger.warning("Using legacy get_ai_suggestions - consider upgrading to enhanced version")
    rule_engine = RuleValidationEngine()
    llm_analyzer = LLMContextAnalyzer()
    return get_ai_suggestions_enhanced(df, logs, rule_engine, llm_analyzer)

def save_processed_file(df, original_filename):
    """Legacy file saving for backward compatibility"""
    logger.warning("Using legacy save_processed_file - consider upgrading to enhanced version")
    validation_summary = {'logs': [], 'stats': {}, 'timestamp': datetime.now().isoformat()}
    return save_processed_file_enhanced(df, original_filename, validation_summary)




