model = BertForPreTraining.from_pretrained('path_to_pretrained_model')
loss = model(input_ids, token_type_ids, attention_mask, lm_labels, next_sent)
loss.backward()