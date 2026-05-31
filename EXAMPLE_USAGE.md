# 📚 EXAMPLE USAGE - Dynamic NLP Prediction System

## Overview
This document shows various ways to use your pure NLP prediction system with different types of inputs.

---

## Example 1: Simple Anxiety Expression

```python
# In Cell 18, change text_input to:
text_input = "aku merasa cemas"

# Run cell (Shift + Enter)
# Expected: NLP model will classify based on learned patterns
```

**Expected Output Characteristics:**
- Raw NLP probability: Based on training data patterns
- No keyword forcing (even though it contains "cemas")
- Diagnosis: Whatever the model learned (not forced to Anxiety)
- Dynamic: Different from results with similar keywords in different contexts

---

## Example 2: Depression Expression

```python
# In Cell 19, change text_input to:
text_input = "saya merasa sangat depresi dan tidak ada energi lagi"

# Run cell
# Expected: Model classifies based on what it learned
```

**Key Point:**
- Previously, "depresi" keyword would bias towards depression class
- Now: Model uses full sentence context to decide
- Result: Pure machine learning, not keyword matching

---

## Example 3: Positive/Normal Expression

```python
# In Cell 20, change text_input to:
text_input = "hari ini saya sangat senang bermain dengan teman"

# Run cell
# Expected: High probability for Normal class
```

**What's Happening:**
- Model analyzes sentence meaning
- Returns confidence for each class
- Displays probability distribution
- No keyword shortcuts applied

---

## Example 4: Complex Mixed Emotion

```python
text_input = """
pagi ini saya merasa sedih dan khawatir tentang pekerjaan saya.
Tapi sore ini saya ada acara dengan keluarga yang menyenangkan.
Jadi perasaanku bercampur aduk sekarang.
"""

# This tests how model handles mixed/complex emotions
# Result: Model's best judgment based on overall meaning
```

---

## Example 5: Specific Symptoms

```python
text_input = "saya susah tidur, kepala pusing, dan tidak bisa fokus bekerja"

# Model sees symptom description
# Classifies based on learned symptom patterns
# NOT forced by any keyword rule
```

---

## Example 6: Very Short Input

```python
text_input = "sedih"

# Even with minimal input, model processes it
# Shows how model handles very brief descriptions
# Demonstrates robustness to text length variation
```

---

## Example 7: Formal/Clinical Language

```python
text_input = "Saya mengalami gejala-gejala depresi yang menggangu aktivitas sehari-hari"

# Model handles both casual and formal Indonesian
# Trained on various linguistic styles
# Same pure NLP approach regardless of formality
```

---

## Example 8: Testing Keyword Independence

### Before (With Bias - Not Used Anymore)
```python
# Old system:
text1 = "saya depresi"  # Would be forced to Depression
text2 = "saya tidak depresi"  # Still biased by "depresi" keyword
```

### After (Pure NLP - Now Used)
```python
# New system:
text1 = "saya depresi"
# Model analyzes meaning

text2 = "saya tidak depresi"
# Model analyzes different meaning -> different result!

# Different results because model understands negation
# Not just keyword matching
```

---

## Example 9: Batch Testing Same Topic

```python
# Test 1
text_input = "saya merasa khawatir"
result1 = run_dynamic_prediction(text_input)

# Test 2  
text_input = "saya merasa sangat khawatir sekali"
result2 = run_dynamic_prediction(text_input)

# Test 3
text_input = "saya tidak merasa khawatir"
result3 = run_dynamic_prediction(text_input)

# Compare results:
# - result1 vs result2: Intensity matters
# - result1 vs result3: Negation changes meaning
# All three handled by pure model, not keyword rules
```

---

## Example 10: High-Risk Input

```python
text_input = """
Saya sudah tidak tahan lagi dengan hidup ini.
Semuanya terasa berat, tidak ada harapan.
Saya hanya ingin istirahat selamanya.
"""

# Model analyzes this as high-risk content
# Treatment recommendation: Yes
# Based on learned patterns, not keyword "ingin mengakhiri hidup" shortcut
```

---

## Testing Patterns

### Pattern 1: Varying Intensity
```python
texts = [
    "saya sedikit cemas",
    "saya cemas",
    "saya sangat cemas",
    "saya sangat sangat cemas sekali"
]

# Run each and compare:
# - Does intensity change probability distribution?
# - How does model handle emphasis words?
# - All by pure NLP, no keyword shortcuts
```

### Pattern 2: Negation
```python
texts = [
    "saya sedih",
    "saya tidak sedih",
    "saya sangat tidak sedih",
]

# Compare results - model should handle negation
# Shows linguistic understanding, not just keyword matching
```

### Pattern 3: Context Variation
```python
texts = [
    "saya sedih",
    "saya sedih setiap hari",
    "saya sedih hanya hari ini",
    "saya sedih karena ujian",
]

# Different contexts -> potentially different classifications
# Model considers full meaning, not just presence of "sedih"
```

### Pattern 4: Length Variation
```python
texts = [
    "sedih",
    "saya sedih",
    "saya merasa sedih akhir-akhir ini",
    "Saya merasa sangat sedih akhir-akhir ini dan ini sangat mengganggu aktivitas saya sehari-hari"
]

# Does length affect predictions?
# How does model handle varying input lengths?
```

---

## Real-World Testing Scenarios

### Scenario 1: Workplace Stress
```python
text_input = """
Pekerjaan saya sangat stress akhir-akhir ini.
Banyak deadline yang mendesak.
Saya merasa beban yang berat.
"""

# Model's pure assessment (no keyword shortcuts)
result = run_dynamic_prediction(text_input)
```

### Scenario 2: Relationship Issues
```python
text_input = """
Hubungan saya dengan pasangan tidak baik.
Kami sering bertengkar.
Saya merasa sendirian meski bersama dia.
"""

# Full context analysis by model
result = run_dynamic_prediction(text_input)
```

### Scenario 3: Health Concerns
```python
text_input = """
Kesehatan saya terganggu.
Saya selalu mengkhawatirkan penyakit.
Tidak bisa tidur nyenyak.
"""

# Model processes health-related concerns
result = run_dynamic_prediction(text_input)
```

### Scenario 4: Positive Update
```python
text_input = """
Hari ini adalah hari yang baik untuk saya.
Saya berhasil mencapai target kerja saya.
Saya merasa bangga dengan diri sendiri.
"""

# Model recognizes positive emotions
result = run_dynamic_prediction(text_input)
```

---

## Comparison: Old vs New Results

### Input: "saya depresi setiap hari"

#### Old System (With Keyword Bias - No Longer Used)
```
- Keyword detected: "depresi"
- Forced bias vector: [0.0, 0.9, 0.0, 0.3]
- Artificial weighting: 0.2 * model + 0.8 * bias
- Result: ALWAYS pushed towards Depression
- Limitation: Keyword always wins, even if context says otherwise
```

#### New System (Pure NLP - Currently Used)
```
- No keyword detection
- Text processed through NLP model
- Raw probabilities from model
- Result: What model actually learned from data
- Benefit: Context matters, negation works, nuance captured
```

---

## How to Experiment

### Step 1: Edit Text
```python
# Open Cell 18 (or 19 or 20)
# Find: text_input = "..."
# Change to your test text
```

### Step 2: Run Cell
```python
# Press Shift + Enter
# Or click Run button (▶)
```

### Step 3: Observe Results
```python
# See probability distribution
# Note the diagnosis
# Check treatment recommendation
# Consider risk level
```

### Step 4: Modify and Retry
```python
# Edit text again
# Run again
# Compare results
# Build intuition about model behavior
```

---

## What to Observe

When testing different inputs, pay attention to:

1. **Probability Distribution**
   - Which class gets highest probability?
   - Are probabilities reasonable given input?
   - Does model make sense?

2. **Consistency**
   - Similar inputs -> similar results?
   - Different inputs -> different results?
   - Model is consistent?

3. **Nuance**
   - Does intensity matter? (sedih vs sangat sedih)
   - Does negation work? (sedih vs tidak sedih)
   - Does context matter? (sedih karena X vs sedih karena Y)

4. **Robustness**
   - Works with short inputs?
   - Works with long inputs?
   - Works with various formality levels?

---

## Advanced Testing

### A/B Testing
```python
# Test two versions of same meaning:
text_a = "saya merasa sedih"
text_b = "perasaan saya sangat duka"

result_a = run_dynamic_prediction(text_a)
result_b = run_dynamic_prediction(text_b)

# Compare: Do synonyms give similar results?
```

### Stress Testing
```python
# Try edge cases:
text_input = ""  # Empty
text_input = "aaaa bbbb cccc"  # Nonsense
text_input = "!!!@@##$$%%"  # Special characters
text_input = "111222333"  # Numbers only

# How does model handle edge cases?
```

### Linguistic Testing
```python
# Test various sentence structures:
"Saya sedih"  # Simple
"Karena apa saya sedih"  # Question
"Apakah saya sedih?"  # Question form
"Aku sedih"  # Different pronoun
"Dia sedih"  # Third person
"Kita sedih"  # Plural

# Model handles various structures?
```

---

## Tips for Best Results

1. **Use Indonesian** - Model trained on Indonesian text
2. **Be Descriptive** - Longer descriptions better than single words
3. **Be Honest** - Accurate input gives better predictions
4. **Try Multiple Times** - Same input always gives same result (model is deterministic)
5. **Experiment** - Try different wordings to see how model responds
6. **Compare Results** - Use multiple test cells to compare

---

## Remember

✅ **Pure NLP** - No keyword shortcuts anymore  
✅ **Fully Dynamic** - Different inputs give different results  
✅ **Model-Based** - Results from trained neural network  
✅ **No Bias** - No artificial forcing of results  
✅ **Easy Testing** - Just edit text and run  

---

## Next Steps

1. **Try one example** - Run any test cell with default text first
2. **Modify text** - Change one input and see results
3. **Experiment** - Try different inputs, observe patterns
4. **Build intuition** - Understand how model behaves
5. **Test with real data** - Try texts relevant to your use case

Good luck testing! 🚀
