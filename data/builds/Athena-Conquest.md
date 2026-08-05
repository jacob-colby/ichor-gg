---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.58
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.29
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.56
    - name: Gauntlet of Thebes
      pick_rate: 0.07
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.18
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.66
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.39
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.44
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.17
      win_rate: 0.68
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.7
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.45
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.31
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.89
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.63
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.7
    alternates:
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.71
    - name: Legionnaire Armor
      pick_rate: 0.06
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-08-01'
  god_win_rate: 0.5341880341880342
  god_matches_won: 125
  god_matches_played: 234
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Oni Hunter''s Garb,
    Gluttonous Grimoire, Shield of the Phoenix, Erosion, Spectral Armor, Draconic
    Scale, Mantle Of Discord, Ethereal Staff, Freya''s Tears, Leviathan''s Hide, Hussar''s
    Wings, Yogi''s Necklace, Soul Gem, Midgardian Mail, Doublet of Binding, Wish-Granting
    Pearl, Gladiator''s Shield, Ancile, Jade Scepter, Chandra''s Grace, Hide of the
    Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.67
      win: 0.56
      pick: 0.18
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.83
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
    Shifter's Shield:
      total: 0.6
      efficiency: 0.58
      win: 0.6
      pick: 0.29
      fit: 0.73
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Gluttonous Grimoire, Soul Gem, Oni Hunter''s Garb, Chandra''s Grace, Rod of Asclepius,
    Spectral Armor, Erosion, Draconic Scale, Ethereal Staff, Phoenix Feather, Mantle
    Of Discord, Lifebinder, Leviathan''s Hide, Yogi''s Necklace, Spirit Robe, Hussar''s
    Wings, Bancroft''s Talon, Wish-Granting Pearl, Midgardian Mail, Freya''s Tears.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.67
      win: 0.56
      pick: 0.18
      fit: 0.36
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.81
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.94
    Shifter's Shield:
      total: 0.59
      efficiency: 0.58
      win: 0.6
      pick: 0.29
      fit: 0.71
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Eye of Providence
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Soul Gem, Eye
    of Providence, Oni Hunter''s Garb, Stone of Binding, Spectral Armor, Void Shield,
    Shield of the Phoenix, Spear of the Magus, Mantle Of Discord, Ethereal Staff,
    Screeching Gargoyle, Erosion, Void Stone, Draconic Scale, The Cosmic Horror, Yogi''s
    Necklace, Leviathan''s Hide, Spear of Desolation, Wish-Granting Pearl, Obsidian
    Shard, Freya''s Tears.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.67
      win: 0.56
      pick: 0.18
      fit: 0.27
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.6
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.32
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.29
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb,
    Eye of Providence, Spectral Armor, Ethereal Staff, Soul Gem, Shield of the Phoenix,
    Mantle Of Discord, Yogi''s Necklace, Bracer of The Abyss, Erosion, Bragi''s Harp,
    Draconic Scale, Death Metal, Leviathan''s Hide, Wish-Granting Pearl, Jade Scepter,
    Rod of Asclepius, Nimble Ring, Midgardian Mail, Chandra''s Grace, Freya''s Tears.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.56
      pick: 0.18
      fit: 0.2
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.23
    Nimble Ring:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.29
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  flex_slots:
  - Shield of the Phoenix
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Shield of the Phoenix,
    Amanita Charm, Gluttonous Grimoire, Soul Gem, Eye of Providence, Oni Hunter''s
    Garb, Freya''s Tears, Ethereal Staff, Chandra''s Grace, Spectral Armor, Chronos''
    Pendant, Mantle Of Discord, Gladiator''s Shield, Erosion, Yogi''s Necklace, Screeching
    Gargoyle, Draconic Scale, Wish-Granting Pearl, Jade Scepter, Death Metal, Leviathan''s
    Hide, Rod of Asclepius, Gem of Focus.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.54
      efficiency: 0.74
      win: 0.44
      pick: 0.21
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.67
      win: 0.56
      pick: 0.18
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shifter's Shield:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.29
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: The Crusher, Berserker''s Shield, Gluttonous
    Grimoire, Jotunn''s Revenge, Runeforged Hammer, Kinetic Cuirass, Hydra''s Lament,
    Amanita Charm, Eye of Providence, Lernaean Bow, Oni Hunter''s Garb, Avenging Blade,
    Golden Blade, Shield Splitter, Eye of the Storm, Pharaoh''s Curse, Soul Gem, Spectral
    Armor, Ethereal Staff, Shield of the Phoenix, Mantle Of Discord, Death Metal,
    Damaru, The Reaper, Yogi''s Necklace, Erosion, Heartseeker, Draconic Scale, Shogun''s
    Ofuda, Bragi''s Harp, Triton''s Conch, Leviathan''s Hide, Arondight, Avatar''s
    Parashu, Wish-Granting Pearl, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.29
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Runeforged Hammer, Kinetic Cuirass, Amanita Charm, Berserker''s
    Shield, Hydra''s Lament, Soul Gem, Ethereal Staff, Eye of Providence, Oni Hunter''s
    Garb, Death Metal, Avenging Blade, Shield Splitter, Spectral Armor, Eye of the
    Storm, Wish-Granting Pearl, Lernaean Bow, Shield of the Phoenix, Jade Scepter,
    Mantle Of Discord, Triton''s Conch, Spear of the Magus, Rod of Asclepius, Pharaoh''s
    Curse, Golden Blade, Yogi''s Necklace, Erosion, Helm of Radiance, Damaru, The
    Reaper, Draconic Scale, The Cosmic Horror, Bragi''s Harp, Freya''s Tears.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.56
      pick: 0.18
      fit: 0.23
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.41
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.29
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Oni
    Hunter''s Garb, Gluttonous Grimoire, Freya''s Tears, Shield of the Phoenix, Erosion,
    Spectral Armor, Draconic Scale, Mantle Of Discord, Ethereal Staff, Leviathan''s
    Hide, Hussar''s Wings, Yogi''s Necklace, Soul Gem, Midgardian Mail, Hide of the
    Nemean Lion, Doublet of Binding, Wish-Granting Pearl, Gladiator''s Shield, Ancile,
    Jade Scepter, Chandra''s Grace.'
  slot_scores:
    Eye of Providence:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.53
      efficiency: 0.74
      win: 0.44
      pick: 0.21
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.83
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
    Shifter's Shield:
      total: 0.6
      efficiency: 0.58
      win: 0.6
      pick: 0.29
      fit: 0.73
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
---
