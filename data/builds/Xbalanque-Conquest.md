---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.55
  slot_order:
  - name: Tyrfing
    pick_rate: 0.56
    win_rate: 0.6
    alternates:
    - name: Dominance
      pick_rate: 0.1
      win_rate: 0.54
    - name: Transcendence
      pick_rate: 0.08
      win_rate: 0.53
  - name: Odysseus' Bow
    pick_rate: 0.43
    win_rate: 0.59
    alternates:
    - name: Dominance
      pick_rate: 0.07
      win_rate: 0.61
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.59
  - name: Hastened Fatalis
    pick_rate: 0.17
    win_rate: 0.61
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.65
    - name: Silverbranch Bow
      pick_rate: 0.13
      win_rate: 0.54
  - name: The Executioner
    pick_rate: 0.2
    win_rate: 0.64
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.15
      win_rate: 0.61
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.58
  - name: Silverbranch Bow
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.64
    - name: Qin's Blade
      pick_rate: 0.1
      win_rate: 0.63
  - name: Hunter's Bow
    pick_rate: 0.12
    win_rate: 0.64
    alternates:
    - name: Manchu Bow
      pick_rate: 0.11
      win_rate: 0.61
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.66
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.55
    win_rate: 0.66
  - name: Death's Toll
    pick_rate: 0.23
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.06
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-08-10'
  god_win_rate: 0.5819742489270386
  god_matches_won: 678
  god_matches_played: 1165
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Damaru
  flex_slots:
  - Damaru
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Damaru, Lernaean Bow, Dominance, Golden Blade,
    The Crusher, Demon Blade, Jotunn''s Revenge, Pharaoh''s Curse, Hydra''s Lament,
    Genji''s Guard, Runeforged Hammer, Tekko-Kagi, Shogun''s Ofuda, Musashi''s Dual
    Swords, The Reaper, Breastplate of Valor, Eros'' Bow, Kinetic Cuirass, Rage, Amanita
    Charm, Oni Hunter''s Garb, Eye of Providence, Avenging Blade, Shield Splitter,
    Barbed Carver.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.33
    Tyrfing:
      total: 0.55
      efficiency: 0.46
      win: 0.6
      pick: 0.56
      fit: 0.64
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.46
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.59
      pick: 0.26
      fit: 0.33
    Damaru:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Musashi's Dual Swords
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Damaru, Berserker''s Shield, Lernaean Bow, Dominance, The Crusher, Demon
    Blade, Golden Blade, Jotunn''s Revenge, Hydra''s Lament, Genji''s Guard, Pharaoh''s
    Curse, Musashi''s Dual Swords, Runeforged Hammer, Tekko-Kagi, Breastplate of Valor,
    The Reaper, Shogun''s Ofuda, Rage, Kinetic Cuirass, Eros'' Bow, Amanita Charm,
    Oni Hunter''s Garb, Eye of Providence, Avenging Blade, Shield Splitter, Barbed
    Carver.'
  slot_scores:
    Tyrfing:
      total: 0.55
      efficiency: 0.46
      win: 0.6
      pick: 0.56
      fit: 0.6
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.57
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.42
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.54
      win: 0.59
      pick: 0.26
      fit: 0.3
    Damaru:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.49
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Pharaoh''s Curse, Genji''s Guard, Oni Hunter''s Garb, Golden Blade, The Reaper,
    Shogun''s Ofuda, The Crusher, Damaru, Lernaean Bow, Chandra''s Grace, Runeforged
    Hammer, Breastplate of Valor, Jotunn''s Revenge, Phoenix Feather, Spectral Armor,
    Freya''s Tears, Shifter''s Shield, Erosion, Umbral Link, Eye of Providence, Eye
    of the Storm, Shield Splitter, Hydra''s Lament, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.52
      efficiency: 0.46
      win: 0.6
      pick: 0.56
      fit: 0.42
    Riptalon:
      total: 0.59
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.58
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.59
      pick: 0.26
      fit: 0.2
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, The Reaper,
    Tekko-Kagi, Damaru, Lernaean Bow, Dominance, Avenging Blade, Genji''s Guard, Heartseeker,
    Golden Blade, Hydra''s Lament, Pharaoh''s Curse, Screeching Gargoyle, Breastplate
    of Valor, Toxic Blade, Titan''s Bane, Runeforged Hammer, Stone of Binding, Kinetic
    Cuirass, Void Shield, Amanita Charm, Demon Blade, Oni Hunter''s Garb, Shogun''s
    Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.53
      efficiency: 0.46
      win: 0.6
      pick: 0.56
      fit: 0.46
    Riptalon:
      total: 0.6
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.64
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.59
      pick: 0.26
      fit: 0.56
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Golden Blade
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Berserker''s Shield, Lernaean Bow, Dominance, Damaru,
    The Crusher, Jotunn''s Revenge, Genji''s Guard, Pharaoh''s Curse, Hydra''s Lament,
    Demon Blade, Runeforged Hammer, Breastplate of Valor, Shogun''s Ofuda, Tekko-Kagi,
    Kinetic Cuirass, Eros'' Bow, Amanita Charm, Toxic Blade, The Reaper, Oni Hunter''s
    Garb, Eye of Providence, Musashi''s Dual Swords, Avenging Blade, Yogi''s Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.57
      efficiency: 0.46
      win: 0.6
      pick: 0.56
      fit: 0.75
    Qin's Blade:
      total: 0.51
      efficiency: 0.37
      win: 0.63
      pick: 0.22
      fit: 0.59
    Riptalon:
      total: 0.6
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.59
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.59
      pick: 0.26
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Riptalon
  flex_slots:
  - Hydra's Lament
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Hydra''s Lament, Breastplate of Valor, Berserker''s Shield, Freya''s Tears, Damaru,
    The Crusher, Lernaean Bow, Shield of the Phoenix, Dominance, Golden Blade, Screeching
    Gargoyle, Pharaoh''s Curse, Chandra''s Grace, Arondight, Kinetic Cuirass, Runeforged
    Hammer, Amanita Charm, Oni Hunter''s Garb, Eye of Providence, Shogun''s Ofuda,
    Demon Blade, Eros'' Bow, The Reaper, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.52
      efficiency: 0.46
      win: 0.6
      pick: 0.56
      fit: 0.4
    Hydra's Lament:
      total: 0.5
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Death Metal
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, Jotunn''s
    Revenge, Death Metal, The Crusher, Berserker''s Shield, Genji''s Guard, Spear
    of the Magus, The Cosmic Horror, Bracer of The Abyss, Spear of Desolation, Hydra''s
    Lament, Damaru, Lernaean Bow, Breastplate of Valor, Blood-Bound Book, Bragi''s
    Harp, Dominance, Bancroft''s Talon, Chronos'' Pendant, Obsidian Shard, Nimble
    Ring, Helm of Radiance, Golden Blade, The Reaper, Rod of Asclepius, Pharaoh''s
    Curse, Jade Scepter, Runeforged Hammer, Gem of Focus, Doom Orb, The World Stone,
    Kinetic Cuirass, Freya''s Tears, Tekko-Kagi, Amanita Charm, Dreamer''s Idol, Ancient
    Signet.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.52
      efficiency: 0.46
      win: 0.6
      pick: 0.56
      fit: 0.39
    Death Metal:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.5
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.39
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.59
      pick: 0.26
      fit: 0.32
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Death Metal,
    The Crusher, Soul Gem, Jotunn''s Revenge, Berserker''s Shield, Damaru, Lernaean
    Bow, Spear of the Magus, Dominance, Bragi''s Harp, The Cosmic Horror, Bracer of
    The Abyss, Genji''s Guard, Golden Blade, Hydra''s Lament, The Reaper, Blood-Bound
    Book, Bancroft''s Talon, Obsidian Shard, Nimble Ring, Tekko-Kagi, Runeforged Hammer,
    Spear of Desolation, Breastplate of Valor, Helm of Radiance, Pharaoh''s Curse,
    Rod of Asclepius, Heartseeker, Kinetic Cuirass, Chronos'' Pendant, Jade Scepter,
    Doom Orb, The World Stone, Amanita Charm, Demon Blade, Dreamer''s Idol.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.34
    Tyrfing:
      total: 0.53
      efficiency: 0.46
      win: 0.6
      pick: 0.56
      fit: 0.48
    Death Metal:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.57
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.43
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.59
      pick: 0.26
      fit: 0.35
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Riptalon
  - Damaru
  - The Crusher
  flex_slots:
  - The Crusher
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Damaru, Lernaean Bow, Golden Blade,
    The Crusher, Demon Blade, Jotunn''s Revenge, Dominance, Pharaoh''s Curse, Hydra''s
    Lament, Genji''s Guard, Runeforged Hammer, Tekko-Kagi, Shogun''s Ofuda, Musashi''s
    Dual Swords, The Reaper, Breastplate of Valor, Eros'' Bow, Kinetic Cuirass, Rage,
    Amanita Charm, Oni Hunter''s Garb, Eye of Providence, Avenging Blade, Shield Splitter,
    Barbed Carver.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.33
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.66
      pick: 0.31
      fit: 0.46
    Damaru:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.49
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.31
  starter: *id001
---
