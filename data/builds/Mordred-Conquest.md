---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.64
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.43
    win_rate: 0.57
    alternates:
    - name: Barbed Carver
      pick_rate: 0.2
      win_rate: 0.45
    - name: Bracer of The Abyss
      pick_rate: 0.08
      win_rate: 0.63
  - name: Shield of the Phoenix
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.14
      win_rate: 0.71
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.67
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.63
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.65
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.31
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.55
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-08-01'
  god_win_rate: 0.5451977401129944
  god_matches_won: 193
  god_matches_played: 354
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Gladiator's Shield
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Gladiator's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Hide of the Nemean Lion, Amanita Charm, Kinetic Cuirass,
    Gluttonous Grimoire, Eye of Providence, Berserker''s Shield, Jotunn''s Revenge,
    The Crusher, Oni Hunter''s Garb, Runeforged Hammer, Freya''s Tears, Shield Splitter,
    Hydra''s Lament, Breastplate of Valor, Soul Gem, Eye of the Storm, Erosion, Spectral
    Armor, Pharaoh''s Curse, Avenging Blade, Yogi''s Necklace, Golden Blade, Death
    Metal, Leviathan''s Hide, Spear of the Magus, Midgardian Mail, Helm of Radiance,
    The Reaper, Lernaean Bow, Stone of Binding, Mantle Of Discord, Rod of Asclepius,
    Damaru, Shogun''s Ofuda, The Cosmic Horror, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.18
      fit: 0.28
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.43
      win: 0.67
      pick: 0.09
      fit: 0.53
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.65
      pick: 0.06
      fit: 0.33
    Shifter's Shield:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.43
      fit: 0.51
    Draconic Scale:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.05
      fit: 0.51
    Amanita Charm:
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Gladiator's Shield
  - Gluttonous Grimoire
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Gladiator's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Draconic Scale, Gluttonous Grimoire, Jotunn''s Revenge, Soul Gem, The Crusher,
    Amanita Charm, Kinetic Cuirass, Berserker''s Shield, Eye of Providence, Hydra''s
    Lament, Breastplate of Valor, Freya''s Tears, Oni Hunter''s Garb, Spear of the
    Magus, Runeforged Hammer, Spear of Desolation, The Cosmic Horror, Shield Splitter,
    Death Metal, Rod of Asclepius, Helm of Radiance, Spectral Armor, Erosion, Eye
    of the Storm, Yogi''s Necklace, Obsidian Shard, The Reaper, Pharaoh''s Curse,
    Chronos'' Pendant, Jade Scepter, Avenging Blade, Golden Blade, Leviathan''s Hide,
    Lernaean Bow, Screeching Gargoyle, Midgardian Mail, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.18
      fit: 0.27
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.43
      win: 0.67
      pick: 0.09
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.43
      fit: 0.38
    Draconic Scale:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.05
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Gladiator's Shield
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Gladiator's Shield
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Draconic Scale, Soul Gem, Hide of the Nemean Lion, Gluttonous
    Grimoire, Kinetic Cuirass, Berserker''s Shield, Jotunn''s Revenge, The Crusher,
    Eye of Providence, Rod of Asclepius, The Reaper, Runeforged Hammer, Oni Hunter''s
    Garb, Chandra''s Grace, Hydra''s Lament, Eye of the Storm, Shield Splitter, Freya''s
    Tears, Breastplate of Valor, Riptalon, Phoenix Feather, Erosion, Spectral Armor,
    Blood-Bound Book, Lifebinder, Avenging Blade, Bancroft''s Talon, Yogi''s Necklace,
    Golden Blade, Pharaoh''s Curse, Death Metal, Leviathan''s Hide, Midgardian Mail,
    Spear of the Magus, Lernaean Bow, Damaru.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.17
      fit: 0.74
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.43
      win: 0.67
      pick: 0.09
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.65
      pick: 0.06
      fit: 0.34
    Shifter's Shield:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.43
      fit: 0.5
    Draconic Scale:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.05
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - Draconic Scale
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Draconic Scale, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Berserker''s Shield, Avenging Blade, Soul Gem,
    Eye of Providence, Stone of Binding, Oni Hunter''s Garb, Screeching Gargoyle,
    Runeforged Hammer, Void Shield, Spear of the Magus, Hydra''s Lament, Freya''s
    Tears, Breastplate of Valor, Shield Splitter, Void Stone, The Reaper, The Cosmic
    Horror, Eye of the Storm, Spear of Desolation, Erosion, Spectral Armor, Heartseeker,
    Yogi''s Necklace, Pharaoh''s Curse, Obsidian Shard, Riptalon, Death Metal, Golden
    Blade, Leviathan''s Hide, Silverbranch Bow, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.18
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.43
      fit: 0.42
    Draconic Scale:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.05
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Bracer of The Abyss
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Bracer of The Abyss
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Berserker''s Shield, Bracer of The Abyss, Gluttonous
    Grimoire, Amanita Charm, Kinetic Cuirass, The Crusher, Golden Blade, Eye of Providence,
    Jotunn''s Revenge, Riptalon, Pharaoh''s Curse, Oni Hunter''s Garb, Soul Gem, Breastplate
    of Valor, Runeforged Hammer, Lernaean Bow, Hydra''s Lament, Freya''s Tears, Silverbranch
    Bow, Shogun''s Ofuda, Tyrfing, Shield Splitter, Spectral Armor, Yogi''s Necklace,
    Erosion, Eye of the Storm, Spear of the Magus, Dominance, Death Metal, Rod of
    Asclepius, Helm of Radiance, Leviathan''s Hide, The Reaper, Avenging Blade, Toxic
    Blade, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.18
      fit: 0.19
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.4
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.57
      win: 0.63
      pick: 0.08
      fit: 0.21
    Shifter's Shield:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.43
      fit: 0.34
    Draconic Scale:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.05
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Gladiator's Shield
  - Hide of the Nemean Lion
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gladiator''s Shield, Draconic Scale,
    Jotunn''s Revenge, Hide of the Nemean Lion, Soul Gem, Gluttonous Grimoire, Breastplate
    of Valor, Amanita Charm, Freya''s Tears, Kinetic Cuirass, Berserker''s Shield,
    Hydra''s Lament, Eye of Providence, The Crusher, Oni Hunter''s Garb, Spear of
    Desolation, Runeforged Hammer, Screeching Gargoyle, Chronos'' Pendant, Chandra''s
    Grace, Spectral Armor, Shield Splitter, Erosion, Spear of the Magus, Yogi''s Necklace,
    Pharaoh''s Curse, Prophetic Cloak, Helm of Radiance, Rod of Asclepius, Eye of
    the Storm, Gem of Focus, The Cosmic Horror, Death Metal, Arondight, Leviathan''s
    Hide, Midgardian Mail, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.18
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Gladiator's Shield:
      total: 0.55
      efficiency: 0.43
      win: 0.67
      pick: 0.09
      fit: 0.66
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.54
      win: 0.65
      pick: 0.06
      fit: 0.26
    Shifter's Shield:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.43
      fit: 0.41
    Draconic Scale:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.05
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Gladiator's Shield
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Gladiator's Shield
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Draconic Scale, Gluttonous Grimoire, Soul
    Gem, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, The Crusher, Berserker''s
    Shield, Eye of Providence, Hydra''s Lament, Oni Hunter''s Garb, Spear of the Magus,
    Breastplate of Valor, Runeforged Hammer, Freya''s Tears, Death Metal, The Cosmic
    Horror, Helm of Radiance, Rod of Asclepius, Spear of Desolation, Shield Splitter,
    Jade Scepter, Spectral Armor, Chronos'' Pendant, Eye of the Storm, Erosion, Obsidian
    Shard, Yogi''s Necklace, Pharaoh''s Curse, Blood-Bound Book, Triton''s Conch,
    Ethereal Staff, Avenging Blade, Bancroft''s Talon, Golden Blade, Wish-Granting
    Pearl, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.18
      fit: 0.25
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.43
      win: 0.67
      pick: 0.09
      fit: 0.46
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.54
      win: 0.65
      pick: 0.06
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.43
      fit: 0.39
    Draconic Scale:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.05
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Gladiator's Shield
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Hide of the Nemean Lion
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Gluttonous Grimoire,
    Amanita Charm, The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield,
    Soul Gem, Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s Lament,
    Death Metal, Spear of the Magus, Shield Splitter, Breastplate of Valor, Freya''s
    Tears, The Cosmic Horror, Helm of Radiance, Rod of Asclepius, Eye of the Storm,
    Spectral Armor, Erosion, Spear of Desolation, Jade Scepter, Yogi''s Necklace,
    Pharaoh''s Curse, Avenging Blade, Golden Blade, Obsidian Shard, Triton''s Conch,
    The Reaper, Lernaean Bow, Chronos'' Pendant, Leviathan''s Hide, Damaru, Ethereal
    Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.18
      fit: 0.23
    Gladiator's Shield:
      total: 0.52
      efficiency: 0.43
      win: 0.67
      pick: 0.09
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.54
      win: 0.65
      pick: 0.06
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.43
      fit: 0.42
    Draconic Scale:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.05
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Eye of Providence, Berserker''s Shield, Jotunn''s Revenge, The Crusher, Oni Hunter''s
    Garb, Runeforged Hammer, Freya''s Tears, Shield Splitter, Hydra''s Lament, Breastplate
    of Valor, Soul Gem, Eye of the Storm, Erosion, Spectral Armor, Draconic Scale,
    Pharaoh''s Curse, Avenging Blade, Yogi''s Necklace, Golden Blade, Death Metal,
    Leviathan''s Hide, Spear of the Magus, Midgardian Mail, Helm of Radiance, The
    Reaper, Lernaean Bow, Stone of Binding, Mantle Of Discord, Rod of Asclepius, Hide
    of the Nemean Lion, Damaru, Shogun''s Ofuda, The Cosmic Horror, Magi''s Cloak.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.51
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
---
