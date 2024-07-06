    498          TORCH_CHECK(idx < inlineSize_, \"TupleElements: invalid index Index = \", idx, \"; Length = \", inlineSize_);
    499          return elementsInline_[idx];
    500        } else {
--->501          return elementsVector_.at(idx);
    502        }
    503      }
    504    
    505      C10_NODISCARD iterator begin() {
    506        if (inlineSize_) {
    507          return elementsInline_;
    508        } else {
    509          return elementsVector_.data()
