---
type: smite-build
god: Cernunnos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Strife
  aspect_pick_rate: 0.46
  aspect_win_rate: 0.54
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.49
    win_rate: 0.55
    alternates:
    - name: Tyrfing
      pick_rate: 0.27
      win_rate: 0.57
    - name: The Reaper
      pick_rate: 0.04
      win_rate: 0.5
  - name: Dagger of Frenzy
    pick_rate: 0.34
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.68
    - name: Odysseus' Bow
      pick_rate: 0.08
      win_rate: 0.5
  - name: Riptalon
    pick_rate: 0.17
    win_rate: 0.48
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.63
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.43
  - name: Dominance
    pick_rate: 0.11
    win_rate: 0.59
    alternates:
    - name: Riptalon
      pick_rate: 0.21
      win_rate: 0.53
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.05
    win_rate: 0.54
    alternates:
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.68
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.61
  - name: Manchu Bow
    pick_rate: 0.08
    win_rate: 0.42
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.55
    - name: Riptalon
      pick_rate: 0.06
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/cernunnos/
  last_verified: '2026-08-01'
  god_win_rate: 0.5460750853242321
  god_matches_won: 160
  god_matches_played: 293
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Blink Rune
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Blink Rune, Lernaean Bow, Hydra''s Lament,
    Berserker''s Shield, Damaru, Runeforged Hammer, Golden Blade, The Reaper, Genji''s
    Guard, Tekko-Kagi, Avenging Blade, Pharaoh''s Curse, Tyrfing, Demon Blade, Heartseeker,
    Breastplate of Valor, Arondight, Oni Hunter''s Garb, Avatar''s Parashu, Yogi''s
    Necklace, Eros'' Bow, Kinetic Cuirass, Barbed Carver, Amanita Charm, Shogun''s
    Ofuda, Spectral Armor.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Berserker's Shield:
      total: 0.52
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Blink Rune
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Damaru
  - Demon Blade
  - The Crusher
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Blink Rune, Lernaean Bow, Damaru, Hydra''s
    Lament, Berserker''s Shield, Runeforged Hammer, Golden Blade, Genji''s Guard,
    The Reaper, Tekko-Kagi, Pharaoh''s Curse, Avenging Blade, Demon Blade, Tyrfing,
    Breastplate of Valor, Heartseeker, Oni Hunter''s Garb, Yogi''s Necklace, Arondight,
    Eros'' Bow, Avatar''s Parashu, Kinetic Cuirass, Amanita Charm, Barbed Carver,
    Shogun''s Ofuda, Musashi''s Dual Swords.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
    Damaru:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Blink Rune
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, Blink Rune, Hydra''s Lament, Lernaean Bow,
    Berserker''s Shield, Runeforged Hammer, Genji''s Guard, Damaru, The Reaper, Golden
    Blade, Breastplate of Valor, Avenging Blade, Tekko-Kagi, Heartseeker, Pharaoh''s
    Curse, Oni Hunter''s Garb, Arondight, Yogi''s Necklace, Avatar''s Parashu, Tyrfing,
    Kinetic Cuirass, Amanita Charm, Shield of the Phoenix, Eros'' Bow, Pendulum Blade,
    Spectral Armor, Chandra''s Grace.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Lernaean Bow:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Berserker's Shield:
      total: 0.51
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.46
    Hydra's Lament:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Blink Rune
  - Berserker's Shield
  - Runeforged Hammer
  - Riptalon
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Blink Rune, Shield of the Phoenix,
    The Reaper, Runeforged Hammer, The Crusher, Jotunn''s Revenge, Kinetic Cuirass,
    Chandra''s Grace, Hydra''s Lament, Lernaean Bow, Genji''s Guard, Pharaoh''s Curse,
    Oni Hunter''s Garb, Golden Blade, Eye of Providence, Damaru, Avenging Blade, Spectral
    Armor, Bloodforge, Yogi''s Necklace, Breastplate of Valor, Shogun''s Ofuda, Phoenix
    Feather, Eye of the Storm, Shield Splitter, Mantle Of Discord.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.38
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.34
    Riptalon:
      total: 0.53
      efficiency: 0.6
      win: 0.48
      pick: 0.17
      fit: 0.64
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Blink Rune
  - Lernaean Bow
  - Avenging Blade
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  flex_slots:
  - Riptalon
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Blink Rune, Avenging Blade, Lernaean
    Bow, Hydra''s Lament, Berserker''s Shield, The Reaper, Damaru, Runeforged Hammer,
    Tekko-Kagi, Golden Blade, Genji''s Guard, Heartseeker, Avatar''s Parashu, Pharaoh''s
    Curse, Tyrfing, Breastplate of Valor, Oni Hunter''s Garb, Titan''s Bane, Screeching
    Gargoyle, Pendulum Blade, Yogi''s Necklace, Arondight, Kinetic Cuirass, Demon
    Blade, Eros'' Bow, Amanita Charm.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Lernaean Bow:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Avenging Blade:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.53
    Riptalon:
      total: 0.52
      efficiency: 0.6
      win: 0.48
      pick: 0.17
      fit: 0.57
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Blink Rune
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Jotunn''s Revenge, Blink Rune, Lernaean
    Bow, Hydra''s Lament, Berserker''s Shield, Damaru, Runeforged Hammer, Golden Blade,
    The Reaper, Genji''s Guard, Tekko-Kagi, Avenging Blade, Pharaoh''s Curse, Tyrfing,
    Demon Blade, Heartseeker, Breastplate of Valor, Arondight, Oni Hunter''s Garb,
    Avatar''s Parashu, Yogi''s Necklace, Eros'' Bow, Kinetic Cuirass, Barbed Carver,
    Amanita Charm, Shogun''s Ofuda, Spectral Armor.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Berserker's Shield:
      total: 0.52
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.23
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Blink Rune
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Reaper
  - Riptalon
  - The Crusher
  flex_slots:
  - Riptalon
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Jotunn''s Revenge, Blink Rune, Runeforged Hammer,
    Hydra''s Lament, Berserker''s Shield, Damaru, Lernaean Bow, Amanita Charm, Golden
    Blade, Avenging Blade, Shield of the Phoenix, Genji''s Guard, Chandra''s Grace,
    Bloodforge, Oni Hunter''s Garb, Yogi''s Necklace, Pharaoh''s Curse, Kinetic Cuirass,
    Heartseeker, Breastplate of Valor, Spectral Armor, Tekko-Kagi, Arondight, Eros''
    Bow, Eye of the Storm, Barbed Carver.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.41
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Reaper:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.53
      efficiency: 0.6
      win: 0.48
      pick: 0.17
      fit: 0.63
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: crit
  slot_order:
  - Blink Rune
  - Berserker's Shield
  - Musashi's Dual Swords
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Blink Rune, Berserker''s Shield, The Crusher, The Reaper, Jotunn''s
    Revenge, Runeforged Hammer, Lernaean Bow, Hydra''s Lament, Damaru, Amanita Charm,
    Golden Blade, Shield of the Phoenix, Genji''s Guard, Chandra''s Grace, Avenging
    Blade, Pharaoh''s Curse, Oni Hunter''s Garb, Bloodforge, Yogi''s Necklace, Kinetic
    Cuirass, Eros'' Bow, Breastplate of Valor, Spectral Armor, Tekko-Kagi, Tyrfing,
    Shogun''s Ofuda, Heartseeker, Eye of Providence.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.28
    Musashi's Dual Swords:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.53
      efficiency: 0.6
      win: 0.48
      pick: 0.17
      fit: 0.66
    Damaru:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
    Demon Blade:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: burst
  slot_order:
  - Blink Rune
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, Blink Rune, The Reaper, Hydra''s Lament,
    Runeforged Hammer, Berserker''s Shield, Amanita Charm, Genji''s Guard, Shield
    of the Phoenix, Lernaean Bow, Damaru, Chandra''s Grace, Avenging Blade, Golden
    Blade, Oni Hunter''s Garb, Bloodforge, Yogi''s Necklace, Breastplate of Valor,
    Kinetic Cuirass, Pharaoh''s Curse, Heartseeker, Spectral Armor, Arondight, Avatar''s
    Parashu, Tekko-Kagi, Eye of Providence, Eros'' Bow.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.35
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.3
    The Reaper:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.41
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: bruiser
  slot_order:
  - Blink Rune
  - Berserker's Shield
  - Shield of the Phoenix
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Blink Rune, Shield of the Phoenix,
    The Reaper, Runeforged Hammer, The Crusher, Jotunn''s Revenge, Kinetic Cuirass,
    Chandra''s Grace, Hydra''s Lament, Genji''s Guard, Oni Hunter''s Garb, Eye of
    Providence, Lernaean Bow, Damaru, Pharaoh''s Curse, Avenging Blade, Golden Blade,
    Bloodforge, Spectral Armor, Yogi''s Necklace, Breastplate of Valor, Phoenix Feather,
    Eye of the Storm, Umbral Link, Shield Splitter, Mantle Of Discord.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.33
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.59
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.35
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: anti-tank
  slot_order:
  - Blink Rune
  - Avenging Blade
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - Blink Rune
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, The Reaper, Avenging Blade, Blink
    Rune, Runeforged Hammer, Hydra''s Lament, Berserker''s Shield, Amanita Charm,
    Lernaean Bow, Damaru, Golden Blade, Shield of the Phoenix, Genji''s Guard, Chandra''s
    Grace, Heartseeker, Bloodforge, Oni Hunter''s Garb, Tekko-Kagi, Avatar''s Parashu,
    Yogi''s Necklace, Pharaoh''s Curse, Kinetic Cuirass, Breastplate of Valor, Spectral
    Armor, Void Shield, Screeching Gargoyle, Titan''s Bane.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Avenging Blade:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.33
    The Reaper:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: model
  slot_order:
  - Blink Rune
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Reaper
  - Riptalon
  - The Crusher
  flex_slots:
  - Blink Rune
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, The Reaper, Jotunn''s Revenge, Blink Rune,
    Runeforged Hammer, Hydra''s Lament, Berserker''s Shield, Damaru, Lernaean Bow,
    Amanita Charm, Golden Blade, Avenging Blade, Shield of the Phoenix, Genji''s Guard,
    Chandra''s Grace, Bloodforge, Oni Hunter''s Garb, Yogi''s Necklace, Pharaoh''s
    Curse, Kinetic Cuirass, Heartseeker, Breastplate of Valor, Spectral Armor, Tekko-Kagi,
    Arondight, Eros'' Bow, Eye of the Storm, Barbed Carver.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.41
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Reaper:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.66
    Riptalon:
      total: 0.53
      efficiency: 0.6
      win: 0.48
      pick: 0.17
      fit: 0.63
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
  aspect: Aspect of Strife
---
