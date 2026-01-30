
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from mainapp.file.upload import handle_uploaded_file
# from mainapp.file.download import download_file
# from mainapp.logic.preprocessing_routes import run_preprocessing_pipeline
# from mainapp.logic.llm_logic import LLMAgent
# import pandas as pd
# import os
# import traceback

# # ===============================
# # 🔹 File Upload + AI Analysis API
# # ===============================
# @csrf_exempt
# def upload_with_ai_view(request):
#     """
#     Upload file + analyze dataset using Mistral AI.
#     """
#     if request.method == "POST" and request.FILES.get("file"):
#         try:
#             uploaded_file = request.FILES["file"]
#             print(f"📥 Received file: {uploaded_file.name} ({uploaded_file.size} bytes)")
            
#             # Validate file type
#             if not uploaded_file.name.lower().endswith('.csv'):
#                 return JsonResponse({
#                     "error": "Only CSV files are supported",
#                     "received_file": uploaded_file.name
#                 }, status=280)
            
#             # Save file
#             saved_path = handle_uploaded_file(uploaded_file)
#             print(f"💾 File saved at: {saved_path}")

#             # Read and analyze CSV
#             try:
#                 df = pd.read_csv(saved_path)
#                 print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
#                 # Perform AI analysis
#                 llm = LLMAgent()
#                 ai_result = llm.analyze_dataset(df)
                
#                 print(f"🤖 AI analysis completed. Status: {ai_result.get('status')}")
#                 print(f"📋 Suggestions: {ai_result.get('suggestions', [])}")

#                 response_data = {
#                     "message": "File uploaded and analyzed successfully!",
#                     "file_info": {
#                         "filename": uploaded_file.name,
#                         "file_path": saved_path,
#                         "rows": df.shape[0],
#                         "columns": df.shape[1],
#                         "columns_list": df.columns.tolist()
#                     },
#                     "ai_analysis": {
#                         "status": ai_result.get("status", "unknown"),
#                         "suggestions": ai_result.get("suggestions", []),
#                         "reasoning": ai_result.get("reasoning", ""),
#                         "connection_verified": ai_result.get("connection_verified", False),
#                         "is_fallback": ai_result.get("is_fallback", False),
#                         "generation_time": ai_result.get("generation_time", 0)
#                     }
#                 }
                
#                 return JsonResponse(response_data)

#             except pd.errors.EmptyDataError:
#                 return JsonResponse({"error": "The CSV file is empty"}, status=280)
#             except pd.errors.ParserError:
#                 return JsonResponse({"error": "Invalid CSV format"}, status=280)
#             except Exception as e:
#                 print(f"❌ CSV processing error: {str(e)}")
#                 return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

#         except Exception as e:
#             print(f"❌ Upload error: {str(e)}")
#             print(traceback.format_exc())
#             return JsonResponse({
#                 "error": f"Upload failed: {str(e)}"
#             }, status=500)

#     return JsonResponse({
#         "error": "No file uploaded",
#         "hint": "Send a POST request with a CSV file"
#     }, status=280)


# # ===============================
# # 🔹 File Download API
# # ===============================
# def download_view(request, filename):
#     """
#     Download processed file.
#     """
#     try:
#         return download_file(filename)
#     except Exception as e:
#         return JsonResponse({"error": f"Download failed: {str(e)}"}, status=404)


# # ===============================
# # 🔹 Preprocessing API
# # ===============================
# @csrf_exempt
# def preprocess_view(request):
#     """
#     Handles CSV file upload and runs preprocessing operations.
#     """
#     if request.method == "POST":
#         file = request.FILES.get("file")
#         operations = request.POST.getlist("operations")

#         if not file:
#             return JsonResponse({"error": "No file uploaded."}, status=280)

#         if not operations:
#             return JsonResponse({"error": "No operations specified."}, status=280)

#         try:
#             print(f"🔧 Starting preprocessing: {operations}")
#             df, logs = run_preprocessing_pipeline(file, operations)
#             preview = df.head(5).to_dict(orient="records")
            
#             response_data = {
#                 "status": "success",
#                 "message": "Preprocessing completed successfully.",
#                 "processed_info": {
#                     "rows": df.shape[0],
#                     "columns": df.shape[1],
#                     "columns_list": df.columns.tolist()
#                 },
#                 "logs": logs,
#                 "preview": preview
#             }
            
#             return JsonResponse(response_data)
            
#         except Exception as e:
#             print(f"❌ Preprocessing error: {str(e)}")
#             return JsonResponse({
#                 "error": f"Preprocessing failed: {str(e)}"
#             }, status=500)

#     return JsonResponse({"error": "Only POST method allowed."}, status=405)


# # ===============================
# # 🔹 Health Check API
# # ===============================
# @csrf_exempt
# def health_check_view(request):
#     """
#     Health check endpoint for the application.
#     """
#     try:
#         llm = LLMAgent()
#         model_status = "connected" if llm.connected else "disconnected"
        
#         return JsonResponse({
#             "status": "healthy",
#             "model_connection": model_status,
#             "service": "Django ML Preprocessing API"
#         })
#     except Exception as e:
#         return JsonResponse({
#             "status": "error",
#             "model_connection": "unknown",
#             "error": str(e)
#         }, status=500)














# #########workingggggggg########
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from mainapp.file.upload import handle_uploaded_file
# from mainapp.file.download import download_file
# from mainapp.logic.preprocessing_routes import run_preprocessing_pipeline
# from mainapp.logic.llm_logic import LLMAgent
# import pandas as pd
# import os
# import traceback

# # ===============================
# # 🔹 File Upload + AI Analysis API
# # ===============================
# @csrf_exempt
# def upload_with_ai_view(request):
#     """
#     Upload file + analyze dataset using Mistral AI.
#     """
#     if request.method == "POST" and request.FILES.get("file"):
#         try:
#             uploaded_file = request.FILES["file"]
#             print(f"📥 Received file: {uploaded_file.name} ({uploaded_file.size} bytes)")
            
#             # Validate file type
#             if not uploaded_file.name.lower().endswith('.csv'):
#                 return JsonResponse({
#                     "error": "Only CSV files are supported",
#                     "received_file": uploaded_file.name
#                 }, status=280)
            
#             # Save file
#             saved_path = handle_uploaded_file(uploaded_file)
#             print(f"💾 File saved at: {saved_path}")

#             # Read and analyze CSV
#             try:
#                 df = pd.read_csv(saved_path)
#                 print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
#                 # Perform AI analysis - USING FAST MODE BY DEFAULT
#                 llm = LLMAgent()
#                 ai_result = llm.analyze_dataset(df, "fast")  # Changed to FAST mode
                
#                 print(f"🤖 AI analysis completed. Status: {ai_result.get('status')}")
                
#                 if ai_result.get("status") == "success":
#                     response_data = {
#                         "message": "File uploaded and analyzed successfully!",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": ai_result.get("status", "unknown"),
#                             "suggestions": ai_result.get("suggestions", []),
#                             "column_operations": ai_result.get("column_operations", {}),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": ai_result.get("connection_verified", False),
#                             "analysis_type": ai_result.get("analysis_type", "fast"),  # Updated
#                             "generation_time": ai_result.get("generation_time", 0),
#                             "is_fallback": False
#                         }
#                     }
#                 else:
#                     # AI analysis failed - return error (NO FALLBACK)
#                     response_data = {
#                         "message": "File uploaded but AI analysis failed",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": "error",
#                             "suggestions": [],
#                             "column_operations": {},
#                             "error": ai_result.get("error", "Unknown error"),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": False,
#                             "is_fallback": False
#                         }
#                     }
                
#                 return JsonResponse(response_data)

#             except pd.errors.EmptyDataError:
#                 return JsonResponse({"error": "The CSV file is empty"}, status=280)
#             except pd.errors.ParserError:
#                 return JsonResponse({"error": "Invalid CSV format"}, status=280)
#             except Exception as e:
#                 print(f"❌ CSV processing error: {str(e)}")
#                 return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

#         except Exception as e:
#             print(f"❌ Upload error: {str(e)}")
#             print(traceback.format_exc())
#             return JsonResponse({
#                 "error": f"Upload failed: {str(e)}"
#             }, status=500)

#     return JsonResponse({
#         "error": "No file uploaded",
#         "hint": "Send a POST request with a CSV file"
#     }, status=280)


# # ===============================
# # 🔹 File Download API
# # ===============================
# def download_view(request, filename):
#     """
#     Download processed file.
#     """
#     try:
#         return download_file(filename)
#     except Exception as e:
#         return JsonResponse({"error": f"Download failed: {str(e)}"}, status=404)


# # ===============================
# # 🔹 Preprocessing API
# # ===============================
# @csrf_exempt
# def preprocess_view(request):
#     """
#     Handles CSV file upload and runs preprocessing operations.
#     """
#     if request.method == "POST":
#         file = request.FILES.get("file")
#         operations = request.POST.getlist("operations")

#         if not file:
#             return JsonResponse({"error": "No file uploaded."}, status=280)

#         if not operations:
#             return JsonResponse({"error": "No operations specified."}, status=280)

#         try:
#             print(f"🔧 Starting preprocessing: {operations}")
#             df, logs = run_preprocessing_pipeline(file, operations)
#             preview = df.head(5).to_dict(orient="records")
            
#             response_data = {
#                 "status": "success",
#                 "message": "Preprocessing completed successfully.",
#                 "processed_info": {
#                     "rows": df.shape[0],
#                     "columns": df.shape[1],
#                     "columns_list": df.columns.tolist()
#                 },
#                 "logs": logs,
#                 "preview": preview
#             }
            
#             return JsonResponse(response_data)
            
#         except Exception as e:
#             print(f"❌ Preprocessing error: {str(e)}")
#             return JsonResponse({
#                 "error": f"Preprocessing failed: {str(e)}"
#             }, status=500)

#     return JsonResponse({"error": "Only POST method allowed."}, status=405)


# # ===============================
# # 🔹 Advanced Analysis API (Optional)
# # ===============================
# @csrf_exempt
# def advanced_analysis_view(request):
#     """
#     Advanced analysis with column-wise operations (when specifically requested)
#     """
#     if request.method == "POST" and request.FILES.get("file"):
#         try:
#             uploaded_file = request.FILES["file"]
#             print(f"📥 Received file for ADVANCED analysis: {uploaded_file.name}")
            
#             if not uploaded_file.name.lower().endswith('.csv'):
#                 return JsonResponse({"error": "Only CSV files are supported"}, status=280)
            
#             saved_path = handle_uploaded_file(uploaded_file)
#             print(f"💾 File saved at: {saved_path}")

#             try:
#                 df = pd.read_csv(saved_path)
#                 print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
#                 # Perform ADVANCED AI analysis - Column-wise
#                 llm = LLMAgent()
#                 ai_result = llm.analyze_dataset(df, "column_wise")  # Advanced mode
                
#                 print(f"🤖 ADVANCED AI analysis completed. Status: {ai_result.get('status')}")
                
#                 if ai_result.get("status") == "success":
#                     response_data = {
#                         "message": "File uploaded and advanced analysis completed!",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": ai_result.get("status", "unknown"),
#                             "suggestions": ai_result.get("suggestions", []),
#                             "column_operations": ai_result.get("column_operations", {}),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": ai_result.get("connection_verified", False),
#                             "analysis_type": ai_result.get("analysis_type", "column_wise"),
#                             "generation_time": ai_result.get("generation_time", 0),
#                             "is_fallback": False
#                         }
#                     }
#                 else:
#                     response_data = {
#                         "message": "File uploaded but advanced analysis failed",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": "error",
#                             "suggestions": [],
#                             "column_operations": {},
#                             "error": ai_result.get("error", "Unknown error"),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": False,
#                             "is_fallback": False
#                         }
#                     }
                
#                 return JsonResponse(response_data)

#             except Exception as e:
#                 print(f"❌ CSV processing error: {str(e)}")
#                 return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

#         except Exception as e:
#             print(f"❌ Upload error: {str(e)}")
#             return JsonResponse({"error": f"Upload failed: {str(e)}"}, status=500)

#     return JsonResponse({"error": "No file uploaded"}, status=280)


# # ===============================
# # 🔹 Health Check API
# # ===============================
# @csrf_exempt
# def health_check_view(request):
#     """
#     Health check endpoint for the application.
#     """
#     try:
#         llm = LLMAgent()
#         model_status = "connected" if llm.connected else "disconnected"
        
#         return JsonResponse({
#             "status": "healthy",
#             "model_connection": model_status,
#             "service": "Django ML Preprocessing API",
#             "modes": {
#                 "fast": "30-60 seconds response time",
#                 "basic": "1-2 minutes response time", 
#                 "column_wise": "3-5 minutes response time"
#             }
#         })
#     except Exception as e:
#         return JsonResponse({
#             "status": "error",
#             "model_connection": "unknown",
#             "error": str(e)
#         }, status=500)


# # ===============================
# # 🔹 Analysis Mode Selection API
# # ===============================
# @csrf_exempt
# def analyze_with_mode_view(request):
#     """
#     Analyze dataset with specific mode selection
#     """
#     if request.method == "POST" and request.FILES.get("file"):
#         try:
#             uploaded_file = request.FILES["file"]
#             analysis_mode = request.POST.get("analysis_mode", "fast")  # Default to fast
            
#             print(f"📥 Received file for {analysis_mode.upper()} analysis: {uploaded_file.name}")
            
#             if not uploaded_file.name.lower().endswith('.csv'):
#                 return JsonResponse({"error": "Only CSV files are supported"}, status=280)
            
#             saved_path = handle_uploaded_file(uploaded_file)
            
#             try:
#                 df = pd.read_csv(saved_path)
#                 print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
#                 # Perform AI analysis with selected mode
#                 llm = LLMAgent()
#                 ai_result = llm.analyze_dataset(df, analysis_mode)
                
#                 print(f"🤖 {analysis_mode.upper()} AI analysis completed. Status: {ai_result.get('status')}")
                
#                 if ai_result.get("status") == "success":
#                     response_data = {
#                         "message": f"File uploaded and {analysis_mode} analysis completed!",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": ai_result.get("status", "unknown"),
#                             "suggestions": ai_result.get("suggestions", []),
#                             "column_operations": ai_result.get("column_operations", {}),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": ai_result.get("connection_verified", False),
#                             "analysis_type": ai_result.get("analysis_type", analysis_mode),
#                             "generation_time": ai_result.get("generation_time", 0),
#                             "is_fallback": False
#                         }
#                     }
#                 else:
#                     response_data = {
#                         "message": f"File uploaded but {analysis_mode} analysis failed",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": "error",
#                             "suggestions": [],
#                             "column_operations": {},
#                             "error": ai_result.get("error", "Unknown error"),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": False,
#                             "is_fallback": False
#                         }
#                     }
                
#                 return JsonResponse(response_data)

#             except Exception as e:
#                 return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

#         except Exception as e:
#             return JsonResponse({"error": f"Upload failed: {str(e)}"}, status=500)

#     return JsonResponse({"error": "No file uploaded"}, status=280)










################################################  new Features  #################################################




# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from mainapp.file.upload import handle_uploaded_file
# from mainapp.file.download import download_file
# from mainapp.logic.preprocessing_routes import run_preprocessing_pipeline
# from mainapp.logic.llm_logic import LLMAgent
# import pandas as pd
# import os
# import traceback

# # ===============================
# # 🔹 File Upload + AI Analysis + Auto Download API
# # ===============================
# @csrf_exempt
# def upload_with_ai_view(request):
#     """
#     Upload file + analyze dataset + auto execute operations + auto download
#     """
#     if request.method == "POST" and request.FILES.get("file"):
#         try:
#             uploaded_file = request.FILES["file"]
#             print(f"📥 Received file: {uploaded_file.name} ({uploaded_file.size} bytes)")
            
#             # Validate file type
#             if not uploaded_file.name.lower().endswith('.csv'):
#                 return JsonResponse({
#                     "error": "Only CSV files are supported",
#                     "received_file": uploaded_file.name
#                 }, status=280)
            
#             # Save file
#             saved_path = handle_uploaded_file(uploaded_file)
#             print(f"💾 File saved at: {saved_path}")

#             # Read and analyze CSV
#             try:
#                 df = pd.read_csv(saved_path)
#                 print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
#                 # Perform AI analysis - USING FAST MODE BY DEFAULT
#                 llm = LLMAgent()
#                 ai_result = llm.analyze_dataset(df, "fast")
                
#                 print(f"🤖 AI analysis completed. Status: {ai_result.get('status')}")
                
#                 if ai_result.get("status") == "success":
#                     # Auto-execute AI suggestions
#                     operations = ai_result.get("suggestions", [])
#                     print(f"🔧 Auto-executing operations: {operations}")
                    
#                     # Run preprocessing pipeline with auto-download
#                     processed_df, logs, download_info = run_preprocessing_pipeline(
#                         saved_path, 
#                         operations, 
#                         uploaded_file.name
#                     )
                    
#                     response_data = {
#                         "message": "File uploaded, analyzed, processed successfully! Download ready!",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": ai_result.get("status", "unknown"),
#                             "suggestions": ai_result.get("suggestions", []),
#                             "column_operations": ai_result.get("column_operations", {}),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": ai_result.get("connection_verified", False),
#                             "analysis_type": ai_result.get("analysis_type", "fast"),
#                             "generation_time": ai_result.get("generation_time", 0),
#                             "is_fallback": False
#                         },
#                         "processing": {
#                             "status": "success",
#                             "executed_operations": operations,
#                             "logs": logs,
#                             "processed_info": {
#                                 "rows": processed_df.shape[0],
#                                 "columns": processed_df.shape[1],
#                                 "columns_list": processed_df.columns.tolist()
#                             }
#                         }
#                     }
                    
#                     # Add download info if available
#                     if download_info:
#                         response_data["download"] = {
#                             "status": "ready",
#                             "filename": download_info["filename"],
#                             "download_url": download_info["download_url"],
#                             "message": "Click to download processed file"
#                         }
                    
#                 else:
#                     # AI analysis failed
#                     response_data = {
#                         "message": "File uploaded but AI analysis failed",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": "error",
#                             "suggestions": [],
#                             "column_operations": {},
#                             "error": ai_result.get("error", "Unknown error"),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": False,
#                             "is_fallback": False
#                         }
#                     }
                
#                 return JsonResponse(response_data)

#             except pd.errors.EmptyDataError:
#                 return JsonResponse({"error": "The CSV file is empty"}, status=280)
#             except pd.errors.ParserError:
#                 return JsonResponse({"error": "Invalid CSV format"}, status=280)
#             except Exception as e:
#                 print(f"❌ CSV processing error: {str(e)}")
#                 return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

#         except Exception as e:
#             print(f"❌ Upload error: {str(e)}")
#             print(traceback.format_exc())
#             return JsonResponse({
#                 "error": f"Upload failed: {str(e)}"
#             }, status=500)

#     return JsonResponse({
#         "error": "No file uploaded",
#         "hint": "Send a POST request with a CSV file"
#     }, status=280)

# # ===============================
# # 🔹 File Download API
# # ===============================
# def download_view(request, filename):
#     """
#     Download processed file.
#     """
#     try:
#         return download_file(filename)
#     except Exception as e:
#         return JsonResponse({"error": f"Download failed: {str(e)}"}, status=404)

# # ===============================
# # 🔹 Preprocessing API
# # ===============================
# @csrf_exempt
# def preprocess_view(request):
#     """
#     Handles CSV file upload and runs preprocessing operations.
#     """
#     if request.method == "POST":
#         file = request.FILES.get("file")
#         operations = request.POST.getlist("operations")

#         if not file:
#             return JsonResponse({"error": "No file uploaded."}, status=280)

#         if not operations:
#             return JsonResponse({"error": "No operations specified."}, status=280)

#         try:
#             print(f"🔧 Starting preprocessing: {operations}")
            
#             # Run preprocessing with auto-download
#             processed_df, logs, download_info = run_preprocessing_pipeline(
#                 file, 
#                 operations, 
#                 file.name
#             )
            
#             preview = processed_df.head(5).to_dict(orient="records")
            
#             response_data = {
#                 "status": "success",
#                 "message": "Preprocessing completed successfully.",
#                 "processed_info": {
#                     "rows": processed_df.shape[0],
#                     "columns": processed_df.shape[1],
#                     "columns_list": processed_df.columns.tolist()
#                 },
#                 "logs": logs,
#                 "preview": preview
#             }
            
#             # Add download info
#             if download_info:
#                 response_data["download"] = {
#                     "filename": download_info["filename"],
#                     "download_url": download_info["download_url"],
#                     "message": "Processed file ready for download"
#                 }
            
#             return JsonResponse(response_data)
            
#         except Exception as e:
#             print(f"❌ Preprocessing error: {str(e)}")
#             return JsonResponse({
#                 "error": f"Preprocessing failed: {str(e)}"
#             }, status=500)

#     return JsonResponse({"error": "Only POST method allowed."}, status=405)

# # ===============================
# # 🔹 Advanced Analysis API
# # ===============================
# @csrf_exempt
# def advanced_analysis_view(request):
#     """
#     Advanced analysis with column-wise operations (when specifically requested)
#     """
#     if request.method == "POST" and request.FILES.get("file"):
#         try:
#             uploaded_file = request.FILES["file"]
#             print(f"📥 Received file for ADVANCED analysis: {uploaded_file.name}")
            
#             if not uploaded_file.name.lower().endswith('.csv'):
#                 return JsonResponse({"error": "Only CSV files are supported"}, status=280)
            
#             saved_path = handle_uploaded_file(uploaded_file)
#             print(f"💾 File saved at: {saved_path}")

#             try:
#                 df = pd.read_csv(saved_path)
#                 print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
#                 # Perform ADVANCED AI analysis - Column-wise
#                 llm = LLMAgent()
#                 ai_result = llm.analyze_dataset(df, "column_wise")
                
#                 print(f"🤖 ADVANCED AI analysis completed. Status: {ai_result.get('status')}")
                
#                 if ai_result.get("status") == "success":
#                     # Auto-execute column-wise operations
#                     column_operations = ai_result.get("column_operations", {})
#                     operations = ai_result.get("suggestions", [])
#                     print(f"🔧 Auto-executing column operations: {column_operations}")
                    
#                     # Run preprocessing with column operations
#                     processed_df, logs, download_info = run_preprocessing_pipeline(
#                         saved_path, 
#                         operations, 
#                         uploaded_file.name
#                     )
                    
#                     response_data = {
#                         "message": "File uploaded and advanced analysis completed!",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": ai_result.get("status", "unknown"),
#                             "suggestions": ai_result.get("suggestions", []),
#                             "column_operations": column_operations,
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": ai_result.get("connection_verified", False),
#                             "analysis_type": ai_result.get("analysis_type", "column_wise"),
#                             "generation_time": ai_result.get("generation_time", 0),
#                             "is_fallback": False
#                         },
#                         "processing": {
#                             "status": "success",
#                             "executed_operations": operations,
#                             "logs": logs,
#                             "processed_info": {
#                                 "rows": processed_df.shape[0],
#                                 "columns": processed_df.shape[1],
#                                 "columns_list": processed_df.columns.tolist()
#                             }
#                         }
#                     }
                    
#                     # Add download info
#                     if download_info:
#                         response_data["download"] = {
#                             "status": "ready",
#                             "filename": download_info["filename"],
#                             "download_url": download_info["download_url"],
#                             "message": "Advanced processed file ready for download"
#                         }
                    
#                 else:
#                     response_data = {
#                         "message": "File uploaded but advanced analysis failed",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": "error",
#                             "suggestions": [],
#                             "column_operations": {},
#                             "error": ai_result.get("error", "Unknown error"),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": False,
#                             "is_fallback": False
#                         }
#                     }
                
#                 return JsonResponse(response_data)

#             except Exception as e:
#                 print(f"❌ CSV processing error: {str(e)}")
#                 return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

#         except Exception as e:
#             print(f"❌ Upload error: {str(e)}")
#             return JsonResponse({"error": f"Upload failed: {str(e)}"}, status=500)

#     return JsonResponse({"error": "No file uploaded"}, status=280)

# # ===============================
# # 🔹 Health Check API
# # ===============================
# @csrf_exempt
# def health_check_view(request):
#     """
#     Health check endpoint for the application.
#     """
#     try:
#         llm = LLMAgent()
#         model_status = "connected" if llm.connected else "disconnected"
        
#         return JsonResponse({
#             "status": "healthy",
#             "model_connection": model_status,
#             "service": "Django ML Preprocessing API",
#             "modes": {
#                 "fast": "30-60 seconds response time",
#                 "basic": "1-2 minutes response time", 
#                 "column_wise": "3-5 minutes response time"
#             }
#         })
#     except Exception as e:
#         return JsonResponse({
#             "status": "error",
#             "model_connection": "unknown",
#             "error": str(e)
#         }, status=500)

# # ===============================
# # 🔹 Analysis Mode Selection API
# # ===============================
# @csrf_exempt
# def analyze_with_mode_view(request):
#     """
#     Analyze dataset with specific mode selection
#     """
#     if request.method == "POST" and request.FILES.get("file"):
#         try:
#             uploaded_file = request.FILES["file"]
#             analysis_mode = request.POST.get("analysis_mode", "fast")
            
#             print(f"📥 Received file for {analysis_mode.upper()} analysis: {uploaded_file.name}")
            
#             if not uploaded_file.name.lower().endswith('.csv'):
#                 return JsonResponse({"error": "Only CSV files are supported"}, status=280)
            
#             saved_path = handle_uploaded_file(uploaded_file)
            
#             try:
#                 df = pd.read_csv(saved_path)
#                 print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
#                 # Perform AI analysis with selected mode
#                 llm = LLMAgent()
#                 ai_result = llm.analyze_dataset(df, analysis_mode)
                
#                 print(f"🤖 {analysis_mode.upper()} AI analysis completed. Status: {ai_result.get('status')}")
                
#                 if ai_result.get("status") == "success":
#                     # Auto-execute operations
#                     operations = ai_result.get("suggestions", [])
#                     print(f"🔧 Auto-executing operations: {operations}")
                    
#                     # Run preprocessing with auto-download
#                     processed_df, logs, download_info = run_preprocessing_pipeline(
#                         saved_path, 
#                         operations, 
#                         uploaded_file.name
#                     )
                    
#                     response_data = {
#                         "message": f"File uploaded and {analysis_mode} analysis completed!",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": ai_result.get("status", "unknown"),
#                             "suggestions": ai_result.get("suggestions", []),
#                             "column_operations": ai_result.get("column_operations", {}),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": ai_result.get("connection_verified", False),
#                             "analysis_type": ai_result.get("analysis_type", analysis_mode),
#                             "generation_time": ai_result.get("generation_time", 0),
#                             "is_fallback": False
#                         },
#                         "processing": {
#                             "status": "success",
#                             "executed_operations": operations,
#                             "logs": logs,
#                             "processed_info": {
#                                 "rows": processed_df.shape[0],
#                                 "columns": processed_df.shape[1],
#                                 "columns_list": processed_df.columns.tolist()
#                             }
#                         }
#                     }
                    
#                     # Add download info
#                     if download_info:
#                         response_data["download"] = {
#                             "status": "ready",
#                             "filename": download_info["filename"],
#                             "download_url": download_info["download_url"],
#                             "message": f"{analysis_mode} processed file ready for download"
#                         }
                    
#                 else:
#                     response_data = {
#                         "message": f"File uploaded but {analysis_mode} analysis failed",
#                         "file_info": {
#                             "filename": uploaded_file.name,
#                             "file_path": saved_path,
#                             "rows": df.shape[0],
#                             "columns": df.shape[1],
#                             "columns_list": df.columns.tolist()
#                         },
#                         "ai_analysis": {
#                             "status": "error",
#                             "suggestions": [],
#                             "column_operations": {},
#                             "error": ai_result.get("error", "Unknown error"),
#                             "reasoning": ai_result.get("reasoning", ""),
#                             "connection_verified": False,
#                             "is_fallback": False
#                         }
#                     }
                
#                 return JsonResponse(response_data)

#             except Exception as e:
#                 return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

#         except Exception as e:
#             return JsonResponse({"error": f"Upload failed: {str(e)}"}, status=500)

#     return JsonResponse({"error": "No file uploaded"}, status=280)




################################################################################################################














from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from mainapp.file.upload import handle_uploaded_file
from mainapp.file.download import download_file
from mainapp.logic.preprocessing_routes import run_preprocessing_pipeline
from mainapp.logic.llm_logic import LLMAgent
import pandas as pd
import os
import traceback

# ===============================
# 🔹 File Upload + AI Analysis + Auto Download API
# ===============================
@csrf_exempt
def upload_with_ai_view(request):
    """
    Upload file + analyze dataset + auto execute column operations + auto download
    """
    if request.method == "POST" and request.FILES.get("file"):
        try:
            uploaded_file = request.FILES["file"]
            print(f"📥 Received file: {uploaded_file.name} ({uploaded_file.size} bytes)")
            
            # Validate file type
            if not uploaded_file.name.lower().endswith('.csv'):
                return JsonResponse({
                    "error": "Only CSV files are supported",
                    "received_file": uploaded_file.name
                }, status=280)
            
            # Save file
            saved_path = handle_uploaded_file(uploaded_file)
            print(f"💾 File saved at: {saved_path}")

            # Read and analyze CSV
            try:
                df = pd.read_csv(saved_path)
                print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
                # Perform AI analysis - USING COLUMN-WISE MODE BY DEFAULT
                llm = LLMAgent()
                ai_result = llm.analyze_dataset(df, "column_wise")
                
                print(f"🤖 AI analysis completed. Status: {ai_result.get('status')}")
                
                if ai_result.get("status") == "success":
                    # Auto-execute AI column-wise suggestions
                    column_operations = ai_result.get("column_operations", {})
                    operations = ai_result.get("suggestions", [])
                    print(f"🔧 Auto-executing column operations: {column_operations}")
                    
                    # Run preprocessing pipeline with column operations and auto-download
                    processed_df, logs, download_info = run_preprocessing_pipeline(
                        saved_path, 
                        operations, 
                        uploaded_file.name,
                        column_operations=column_operations  # NEW: Pass column operations
                    )
                    
                    response_data = {
                        "message": "File uploaded, analyzed, processed successfully! Download ready!",
                        "file_info": {
                            "filename": uploaded_file.name,
                            "file_path": saved_path,
                            "rows": df.shape[0],
                            "columns": df.shape[1],
                            "columns_list": df.columns.tolist()
                        },
                        "ai_analysis": {
                            "status": ai_result.get("status", "unknown"),
                            "suggestions": ai_result.get("suggestions", []),
                            "column_operations": column_operations,  # This is now the main output
                            "reasoning": ai_result.get("reasoning", ""),
                            "connection_verified": ai_result.get("connection_verified", False),
                            "analysis_type": ai_result.get("analysis_type", "column_wise"),
                            "generation_time": ai_result.get("generation_time", 0),
                            "is_fallback": False
                        },
                        "processing": {
                            "status": "success",
                            "executed_operations": operations,
                            "column_operations_executed": column_operations,  # NEW: Show what was executed
                            "logs": logs,
                            "processed_info": {
                                "rows": processed_df.shape[0],
                                "columns": processed_df.shape[1],
                                "columns_list": processed_df.columns.tolist()
                            }
                        }
                    }
                    
                    # Add download info if available
                    if download_info:
                        response_data["download"] = {
                            "status": "ready",
                            "filename": download_info["filename"],
                            "download_url": download_info["download_url"],
                            "message": "Click to download processed file"
                        }
                    
                else:
                    # AI analysis failed
                    response_data = {
                        "message": "File uploaded but AI analysis failed",
                        "file_info": {
                            "filename": uploaded_file.name,
                            "file_path": saved_path,
                            "rows": df.shape[0],
                            "columns": df.shape[1],
                            "columns_list": df.columns.tolist()
                        },
                        "ai_analysis": {
                            "status": "error",
                            "suggestions": [],
                            "column_operations": {},
                            "error": ai_result.get("error", "Unknown error"),
                            "reasoning": ai_result.get("reasoning", ""),
                            "connection_verified": False,
                            "is_fallback": False
                        }
                    }
                
                return JsonResponse(response_data)

            except pd.errors.EmptyDataError:
                return JsonResponse({"error": "The CSV file is empty"}, status=280)
            except pd.errors.ParserError:
                return JsonResponse({"error": "Invalid CSV format"}, status=280)
            except Exception as e:
                print(f"❌ CSV processing error: {str(e)}")
                return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

        except Exception as e:
            print(f"❌ Upload error: {str(e)}")
            print(traceback.format_exc())
            return JsonResponse({
                "error": f"Upload failed: {str(e)}"
            }, status=500)

    return JsonResponse({
        "error": "No file uploaded",
        "hint": "Send a POST request with a CSV file"
    }, status=280)

# ===============================
# 🔹 File Download API
# ===============================
def download_view(request, filename):
    """
    Download processed file.
    """
    try:
        return download_file(filename)
    except Exception as e:
        return JsonResponse({"error": f"Download failed: {str(e)}"}, status=404)

# ===============================
# 🔹 Preprocessing API
# ===============================
@csrf_exempt
def preprocess_view(request):
    """
    Handles CSV file upload and runs preprocessing operations.
    """
    if request.method == "POST":
        file = request.FILES.get("file")
        operations = request.POST.getlist("operations")

        if not file:
            return JsonResponse({"error": "No file uploaded."}, status=280)

        if not operations:
            return JsonResponse({"error": "No operations specified."}, status=280)

        try:
            print(f"🔧 Starting preprocessing: {operations}")
            
            # Run preprocessing with auto-download
            processed_df, logs, download_info = run_preprocessing_pipeline(
                file, 
                operations, 
                file.name
            )
            
            preview = processed_df.head(5).to_dict(orient="records")
            
            response_data = {
                "status": "success",
                "message": "Preprocessing completed successfully.",
                "processed_info": {
                    "rows": processed_df.shape[0],
                    "columns": processed_df.shape[1],
                    "columns_list": processed_df.columns.tolist()
                },
                "logs": logs,
                "preview": preview
            }
            
            # Add download info
            if download_info:
                response_data["download"] = {
                    "filename": download_info["filename"],
                    "download_url": download_info["download_url"],
                    "message": "Processed file ready for download"
                }
            
            return JsonResponse(response_data)
            
        except Exception as e:
            print(f"❌ Preprocessing error: {str(e)}")
            return JsonResponse({
                "error": f"Preprocessing failed: {str(e)}"
            }, status=500)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)

# ===============================
# 🔹 Health Check API
# ===============================
@csrf_exempt
def health_check_view(request):
    """
    Health check endpoint for the application.
    """
    try:
        llm = LLMAgent()
        model_status = "connected" if llm.connected else "disconnected"
        
        return JsonResponse({
            "status": "healthy",
            "model_connection": model_status,
            "service": "Django ML Preprocessing API",
            "mode": "column_wise_operations",
            "description": "Fast column-wise preprocessing operations only"
        })
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "model_connection": "unknown",
            "error": str(e)
        }, status=500)

# ===============================
# 🔹 Analysis Mode Selection API (Simplified)
# ===============================
@csrf_exempt
def analyze_with_mode_view(request):
    """
    Analyze dataset with column-wise mode only
    """
    if request.method == "POST" and request.FILES.get("file"):
        try:
            uploaded_file = request.FILES["file"]
            
            print(f"📥 Received file for COLUMN-WISE analysis: {uploaded_file.name}")
            
            if not uploaded_file.name.lower().endswith('.csv'):
                return JsonResponse({"error": "Only CSV files are supported"}, status=280)
            
            saved_path = handle_uploaded_file(uploaded_file)
            
            try:
                df = pd.read_csv(saved_path)
                print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
                # Perform AI analysis with column-wise mode
                llm = LLMAgent()
                ai_result = llm.analyze_dataset(df, "column_wise")
                
                print(f"🤖 COLUMN-WISE AI analysis completed. Status: {ai_result.get('status')}")
                
                if ai_result.get("status") == "success":
                    # Auto-execute column operations
                    column_operations = ai_result.get("column_operations", {})
                    operations = ai_result.get("suggestions", [])
                    print(f"🔧 Auto-executing column operations: {column_operations}")
                    
                    # Run preprocessing with column operations and auto-download
                    processed_df, logs, download_info = run_preprocessing_pipeline(
                        saved_path, 
                        operations, 
                        uploaded_file.name,
                        column_operations=column_operations
                    )
                    
                    response_data = {
                        "message": "File uploaded and column-wise analysis completed!",
                        "file_info": {
                            "filename": uploaded_file.name,
                            "file_path": saved_path,
                            "rows": df.shape[0],
                            "columns": df.shape[1],
                            "columns_list": df.columns.tolist()
                        },
                        "ai_analysis": {
                            "status": ai_result.get("status", "unknown"),
                            "suggestions": ai_result.get("suggestions", []),
                            "column_operations": column_operations,
                            "reasoning": ai_result.get("reasoning", ""),
                            "connection_verified": ai_result.get("connection_verified", False),
                            "analysis_type": ai_result.get("analysis_type", "column_wise"),
                            "generation_time": ai_result.get("generation_time", 0),
                            "is_fallback": False
                        },
                        "processing": {
                            "status": "success",
                            "executed_operations": operations,
                            "column_operations_executed": column_operations,
                            "logs": logs,
                            "processed_info": {
                                "rows": processed_df.shape[0],
                                "columns": processed_df.shape[1],
                                "columns_list": processed_df.columns.tolist()
                            }
                        }
                    }
                    
                    # Add download info
                    if download_info:
                        response_data["download"] = {
                            "status": "ready",
                            "filename": download_info["filename"],
                            "download_url": download_info["download_url"],
                            "message": "Column-wise processed file ready for download"
                        }
                    
                else:
                    response_data = {
                        "message": "File uploaded but column-wise analysis failed",
                        "file_info": {
                            "filename": uploaded_file.name,
                            "file_path": saved_path,
                            "rows": df.shape[0],
                            "columns": df.shape[1],
                            "columns_list": df.columns.tolist()
                        },
                        "ai_analysis": {
                            "status": "error",
                            "suggestions": [],
                            "column_operations": {},
                            "error": ai_result.get("error", "Unknown error"),
                            "reasoning": ai_result.get("reasoning", ""),
                            "connection_verified": False,
                            "is_fallback": False
                        }
                    }
                
                return JsonResponse(response_data)

            except Exception as e:
                return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

        except Exception as e:
            return JsonResponse({"error": f"Upload failed: {str(e)}"}, status=500)

    return JsonResponse({"error": "No file uploaded"}, status=280)

# ===============================
# 🔹 Advanced Analysis API (Fixed - Added missing function)
# ===============================
@csrf_exempt
def advanced_analysis_view(request):
    """
    Advanced analysis with column-wise operations (when specifically requested)
    """
    if request.method == "POST" and request.FILES.get("file"):
        try:
            uploaded_file = request.FILES["file"]
            print(f"📥 Received file for ADVANCED analysis: {uploaded_file.name}")
            
            if not uploaded_file.name.lower().endswith('.csv'):
                return JsonResponse({"error": "Only CSV files are supported"}, status=280)
            
            saved_path = handle_uploaded_file(uploaded_file)
            print(f"💾 File saved at: {saved_path}")

            try:
                df = pd.read_csv(saved_path)
                print(f"📊 CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
                
                # Perform ADVANCED AI analysis - Column-wise
                llm = LLMAgent()
                ai_result = llm.analyze_dataset(df, "column_wise")
                
                print(f"🤖 ADVANCED AI analysis completed. Status: {ai_result.get('status')}")
                
                if ai_result.get("status") == "success":
                    # Auto-execute column-wise operations
                    column_operations = ai_result.get("column_operations", {})
                    operations = ai_result.get("suggestions", [])
                    print(f"🔧 Auto-executing column operations: {column_operations}")
                    
                    # Run preprocessing with column operations
                    processed_df, logs, download_info = run_preprocessing_pipeline(
                        saved_path, 
                        operations, 
                        uploaded_file.name,
                        column_operations=column_operations
                    )
                    
                    response_data = {
                        "message": "File uploaded and advanced analysis completed!",
                        "file_info": {
                            "filename": uploaded_file.name,
                            "file_path": saved_path,
                            "rows": df.shape[0],
                            "columns": df.shape[1],
                            "columns_list": df.columns.tolist()
                        },
                        "ai_analysis": {
                            "status": ai_result.get("status", "unknown"),
                            "suggestions": ai_result.get("suggestions", []),
                            "column_operations": column_operations,
                            "reasoning": ai_result.get("reasoning", ""),
                            "connection_verified": ai_result.get("connection_verified", False),
                            "analysis_type": ai_result.get("analysis_type", "column_wise"),
                            "generation_time": ai_result.get("generation_time", 0),
                            "is_fallback": False
                        },
                        "processing": {
                            "status": "success",
                            "executed_operations": operations,
                            "logs": logs,
                            "processed_info": {
                                "rows": processed_df.shape[0],
                                "columns": processed_df.shape[1],
                                "columns_list": processed_df.columns.tolist()
                            }
                        }
                    }
                    
                    # Add download info
                    if download_info:
                        response_data["download"] = {
                            "status": "ready",
                            "filename": download_info["filename"],
                            "download_url": download_info["download_url"],
                            "message": "Advanced processed file ready for download"
                        }
                    
                else:
                    response_data = {
                        "message": "File uploaded but advanced analysis failed",
                        "file_info": {
                            "filename": uploaded_file.name,
                            "file_path": saved_path,
                            "rows": df.shape[0],
                            "columns": df.shape[1],
                            "columns_list": df.columns.tolist()
                        },
                        "ai_analysis": {
                            "status": "error",
                            "suggestions": [],
                            "column_operations": {},
                            "error": ai_result.get("error", "Unknown error"),
                            "reasoning": ai_result.get("reasoning", ""),
                            "connection_verified": False,
                            "is_fallback": False
                        }
                    }
                
                return JsonResponse(response_data)

            except Exception as e:
                print(f"❌ CSV processing error: {str(e)}")
                return JsonResponse({"error": f"Error processing CSV: {str(e)}"}, status=500)

        except Exception as e:
            print(f"❌ Upload error: {str(e)}")
            return JsonResponse({"error": f"Upload failed: {str(e)}"}, status=500)

    return JsonResponse({"error": "No file uploaded"}, status=280)