//
//  ParagraphView.swift
//  MediCat
//
//  Created by Nikolas Psathakis on 18.11.23.
//

import SwiftUI

struct ParagraphView: View {
    var item: ParagraphItem
    @State private var isDoubleTapped = false

    var body: some View {
        VStack(alignment: .leading) {
            Text("Paragraph \(item.paragraph_number)")
                .font(.headline)
            Text(item.original_paragraph)
                .font(.body)
            Text("Relevance Score: \(item.relevance_score, specifier: "%.2f")")
                .font(.subheadline)
                .foregroundColor(.gray)
        }
        .padding()
        .background(RoundedRectangle(cornerRadius: 10).fill(Color.white))
        .shadow(radius: 5)
        .blur(radius: isDoubleTapped ? 10 : 0)
        .overlay(
            isDoubleTapped ? Image(systemName: "checkmark.circle.fill")
                .font(.largeTitle)
                .foregroundColor(.green)
                .transition(.scale) : nil
        )
        .onTapGesture(count: 2) {
            withAnimation {
                isDoubleTapped.toggle()
            }
        }
    }
}


